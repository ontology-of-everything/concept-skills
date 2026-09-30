#!/usr/bin/env python3
"""Publish one English skill using the catalog's title, version, categories, and topics.

Defaults to a local plan. --publish performs an identity check, runs QA, uploads
the complete bundle (including dot-directory manifests), and submits a release.
"""

import argparse
import hashlib
import importlib.util
import json
import mimetypes
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = "https://clawhub.ai"
OWNER = "agenticweb4"
spec = importlib.util.spec_from_file_location("skill_catalog", ROOT / "tools/skill-catalog.py")
catalog_tools = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog_tools)


def bundle_files(root):
    files = []
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Symlink in bundle: {path}")
        if not path.is_file():
            continue
        if path.name == ".DS_Store" or path.name.startswith(".env") or "node_modules" in path.parts:
            raise ValueError(f"Unexpected file in install payload: {path}")
        data = path.read_bytes()
        if len(data) > 10 * 1024 * 1024:
            raise ValueError(f"File exceeds ClawHub upload limit: {path}")
        files.append({"path": str(path.relative_to(root)), "size": len(data), "sha256": hashlib.sha256(data).hexdigest(), "contentType": mimetypes.guess_type(path.name)[0] or "text/plain"})
    if sum(f["size"] for f in files) > 50 * 1024 * 1024:
        raise ValueError("Bundle exceeds ClawHub upload limit")
    if not any(f["path"] == "SKILL.md" for f in files):
        raise ValueError("Bundle is missing SKILL.md")
    return files


def request(path, token=None, body=None):
    headers = {"User-Agent": "concept-skills-publisher"}
    if token:
        headers["Authorization"] = "Bearer " + token
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode()
    req = urllib.request.Request(REGISTRY + path, headers=headers, data=data)
    try:
        with urllib.request.urlopen(req, timeout=60) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        if error.code == 404 and body is None:
            return None
        raise RuntimeError(f"ClawHub HTTP {error.code}: {error.read().decode()}") from None


def check_remote_identity(remote, slug, version):
    if remote is None:
        return
    actual = (remote.get("skill") or {}).get("slug")
    if actual != slug:
        raise ValueError(f"{slug} resolves to {actual}; stop to protect the other skill")
    if (remote.get("owner") or {}).get("handle", "").lower() != OWNER:
        raise ValueError("Unexpected ClawHub publisher")
    if (remote.get("latestVersion") or {}).get("version") == version:
        raise ValueError(f"{slug}@{version} is already published; update the catalog and QA version first, or edit only catalog metadata in ClawHub Settings")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("skill", help="Exact English catalog ID")
    parser.add_argument("--notes-file", type=Path, help="UTF-8 release notes; required with --publish")
    parser.add_argument("--publish", action="store_true", help="Upload and submit this release")
    args = parser.parse_args()
    catalog = catalog_tools.load_catalog()
    entry = next((s for s in catalog["skills"] if s["id"] == args.skill), None)
    if not entry or entry["language"] != "en":
        parser.error("Choose an English skill from docs/catalog.yml")
    metadata = entry["clawhub"]
    if metadata.get("enabled", True) is False:
        parser.error(metadata.get("reason", "Publication deferred in catalog"))
    folder = ROOT / entry["path"]
    files = bundle_files(folder)
    payload = {"slug": entry["id"], "displayName": entry.get("display_title", entry["display_name"]), "ownerHandle": OWNER, "version": entry["version"], "categories": metadata["categories"], "topics": metadata["topics"], "tags": ["latest"]}
    if not args.publish:
        print(json.dumps({"status": "plan", **payload, "files": files}, ensure_ascii=False, indent=2))
        return
    if not args.notes_file or not args.notes_file.read_text().strip():
        parser.error("--notes-file must contain the release changelog")
    subprocess.run(["python3", str(ROOT / "tools/skill-catalog.py")], check=True)
    subprocess.run([str(ROOT / entry["qa"] / "validate.sh")], check=True, cwd=ROOT)
    token = subprocess.check_output(["clawhub", "token"], text=True).strip()
    query = urllib.parse.urlencode({"ownerHandle": OWNER})
    remote = request(f"/api/v1/skills/{entry['id']}?{query}", token)
    check_remote_identity(remote, entry["id"], entry["version"])
    uploaded = []
    for file in files:
        data = (folder / file["path"]).read_bytes()
        if hashlib.sha256(data).hexdigest() != file["sha256"]:
            raise ValueError("Bundle changed after validation")
        ticket = request("/api/v1/skills/-/upload-url", token, file)
        upload = urllib.request.Request(ticket["uploadUrl"], data=data, headers={"Content-Type": file["contentType"]})
        with urllib.request.urlopen(upload, timeout=60) as response:
            storage = json.load(response)
        uploaded.append({**file, "storageId": storage["storageId"], "uploadTicket": ticket["uploadTicket"]})
    result = request("/api/v1/skills", token, {**payload, "changelog": args.notes_file.read_text().strip(), "acceptLicenseTerms": True, "files": uploaded})
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result.get("publicationStatus") != "published":
        print("Submission is not confirmed published. Verify the public version, title, categories, topics, and complete file hashes before announcing completion.")


if __name__ == "__main__":
    main()
