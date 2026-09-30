#!/usr/bin/env python3
"""Validate the catalog and generate its human-facing classification views."""

import argparse
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = set("integrations automation research development productivity communication creative knowledge agents operations security finance lifestyle other".split())
RESERVED_TOPICS = set("approved audited certified clawhub community curated endorsed featured official officials openclaw recommended staff-pick trusted trusted-publisher verified".split())
START = "<!-- skill-catalog:start -->"
END = "<!-- skill-catalog:end -->"


def load_catalog():
    catalog = yaml.safe_load((ROOT / "docs/catalog.yml").read_text())
    entries = {s["id"]: s for s in catalog["skills"]}
    if len(entries) != len(catalog["skills"]):
        raise ValueError("Duplicate skill IDs")
    for skill in entries.values():
        slug = skill["id"]
        if skill["domain"] not in catalog["domains"]:
            raise ValueError(f"{slug}: unknown domain")
        pair = entries[skill["translation_of"]]
        if pair["domain"] != skill["domain"]:
            raise ValueError(f"{slug}: localized domains differ")
        if not (ROOT / skill["path"] / "SKILL.md").is_file():
            raise ValueError(f"{slug}: missing skill")
        if skill["language"] != "en":
            if "clawhub" in skill.get("marketplaces", []):
                raise ValueError(f"{slug}: Chinese editions must not publish to ClawHub")
            continue
        meta = skill["clawhub"]
        slug = meta.get("slug", skill["id"])
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            raise ValueError(f"{skill['id']}: invalid ClawHub slug {slug!r}")
        categories, topics = meta["categories"], meta["topics"]
        if not 1 <= len(categories) <= 3 or not set(categories) <= CATEGORIES:
            raise ValueError(f"{slug}: invalid ClawHub categories")
        if not 1 <= len(topics) <= 5 or len(set(topics)) != len(topics):
            raise ValueError(f"{slug}: invalid topic count or duplicate topics")
        for topic in topics:
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", topic) or len(topic) > 48 or topic in RESERVED_TOPICS:
                raise ValueError(f"{slug}: invalid topic {topic!r}")
        if (ROOT / skill["qa"] / "VERSION").read_text().strip() != skill["version"]:
            raise ValueError(f"{slug}: catalog and QA versions differ")
    return catalog


def generated_views(catalog):
    skills = catalog["skills"]
    groups = []
    readmes = {}
    for lang, filename in [("en", "README.md"), ("zh-CN", "README-CN.md")]:
        cn = lang == "zh-CN"
        lines = [START, ""]
        lines += ["按主要解决的问题分类；系列名称用于展示。" if cn else "Classified by the primary problem each skill solves; family names identify the series.", ""]
        for domain, spec in catalog["domains"].items():
            lines += ["### " + spec["name_zh" if cn else "name"], "", spec["description_zh" if cn else "description"], ""]
            lines += ["| 技能 | 版本 | ClawHub 分类 |" if cn else "| Skill | Version | ClawHub category |", "| --- | --- | --- |"]
            for skill in skills:
                if skill["domain"] != domain or skill["language"] != lang:
                    continue
                base = next(s for s in skills if s["id"] == skill["translation_of"]) if cn else skill
                meta = base["clawhub"]
                status = ", ".join(meta["categories"])
                if meta.get("enabled", True) is False:
                    status += "（暂缓发布）" if cn else " (publication deferred)"
                locale = "cn" if cn else "en"
                lines.append(f"| [{skill['display_name']}](docs/skills/{locale}/{skill['id']}.md) | {skill['version']} | {status} |")
            lines.append("")
        lines.append(END)
        readmes[filename] = "\n".join(lines)
    for domain, spec in catalog["domains"].items():
        groups.append({"title": spec["name"], "description": spec["description"], "skills": [s["id"] for s in skills if s["domain"] == domain]})
    return readmes, {"$schema": "https://skills.sh/schemas/skills.sh.schema.json", "notGrouped": "bottom", "groupings": groups}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Update generated README sections and skills.sh.json")
    args = parser.parse_args()
    catalog = load_catalog()
    readmes, groups = generated_views(catalog)
    drift = []
    for filename, generated in readmes.items():
        path = ROOT / filename
        text = path.read_text()
        if text.count(START) != 1 or text.count(END) != 1:
            raise ValueError(f"{filename}: expected one generated catalog block")
        start, end = text.index(START), text.index(END) + len(END)
        if text[start:end] != generated:
            if args.write:
                path.write_text(text[:start] + generated + text[end:])
            else:
                drift.append(filename)
    path = ROOT / "skills.sh.json"
    if json.loads(path.read_text()) != groups:
        if args.write:
            path.write_text(json.dumps(groups, ensure_ascii=False, indent=2) + "\n")
        else:
            drift.append(str(path.relative_to(ROOT)))
    if drift:
        raise ValueError("Catalog views are stale; run tools/skill-catalog.py --write: " + ", ".join(drift))
    print(f"OK: {len(catalog['domains'])} domains, {len(catalog['skills'])} localized entries; catalog views agree")


if __name__ == "__main__":
    main()
