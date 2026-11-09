#!/usr/bin/env python3
"""Check the single concept entry and exercise its checker on packaged examples."""

import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile

import yaml


ROOT = Path(__file__).resolve().parents[1]
MODES = ("design", "settle", "prd", "build", "review", "guard", "refine", "explain")


def run(checker, paths):
    result = subprocess.run(
        [sys.executable, str(checker), *map(str, paths), "--json"],
        capture_output=True, text=True,
    )
    return result.returncode, json.loads(result.stdout)


def require(condition, message):
    if not condition:
        raise SystemExit("FAIL: " + message)


def check_package(package):
    require(not (package / "runtime").exists(), "concept must not carry hook runtime")
    entry = (package / "SKILL.md").read_text()
    policy = yaml.safe_load((package / "agents/openai.yaml").read_text())
    require(policy["policy"]["allow_implicit_invocation"] is False, "concept must be explicit-only")
    for mode in MODES:
        route = re.search(rf"^\|\s*`{mode}`\s*\|\s*\[[^\]]+\]\(([^)]+)\)", entry, re.M)
        require(route is not None, f"missing mode route: {mode}")
        require((package / route[1]).is_file(), f"missing workflow: {mode}")

    decision_text = (package / "references/shared/artifacts/decisions.md").read_text()
    records = re.findall(r"```yaml\n(.*?)\n```", decision_text, re.S)
    require(len(records) == 1, "one decision-record shape is required")
    record = yaml.safe_load(records[0])
    require(set(record) == {"id", "status", "claim", "basis", "alternative", "counterexample", "acceptance"}, "decision-record fields differ")
    require(record["status"] in {"confirmed", "proposed", "inferred", "open"}, "unknown decision status")
    require(set(record["acceptance"]) == {"setup", "stimulus", "observe"}, "acceptance fields differ")

    checker = package / "scripts/concept_lint.py"
    samples = []
    for name in ("shared/model/spec-format.md", "shared/learning/examples.md"):
        text = (package / "references" / name).read_text()
        samples.extend(body for body in re.findall(r"```(?:text|markdown)\n(.*?)\n```", text, re.S)
                       if re.match(r"# (concept|app) ", body))
    require(len(samples) >= 5, "missing specification examples")
    with tempfile.TemporaryDirectory(prefix="concept-package-") as directory:
        empty = Path(directory) / "empty-concept.md"
        empty.write_text("# concept Empty\ncoverage: complete\n" +
                         "\n".join(f"## {name}" for name in ("purpose", "state", "actions", "operational principle")))
        code, report = run(checker, [empty])
        require(code == 1, f"empty concept sections were accepted: {report}")
        paths = []
        for index, sample in enumerate(samples):
            path = Path(directory) / f"sample-{index}.md"
            path.write_text(sample + "\n")
            paths.append(path)
        before = {p: hashlib.sha256(p.read_bytes()).digest() for p in paths}
        code, report = run(checker, paths)
        require(code == 0 and report["status"] == "format_checked", f"packaged syntax failed: {report}")
        require(before == {p: hashlib.sha256(p.read_bytes()).digest() for p in paths}, "checker changed its input")

        concept = next(sample for sample in samples if sample.startswith("# concept "))
        app = next(sample for sample in samples if sample.startswith("# app "))
        cases = (
            (concept.replace("## state", "## missing-state", 1), 1, "format_error"),
            (app.replace("then {", "therefore {", 1), 1, "format_error"),
            (concept.replace("## operational principle", "## principle", 1), 3, "not_checked"),
        )
        for text, expected_code, expected_status in cases:
            path = Path(directory) / "case.md"
            path.write_text(text)
            code, report = run(checker, [path])
            require((code, report["status"]) == (expected_code, expected_status), f"checker classified sample incorrectly: {report}")
        code, report = run(checker, [Path(directory) / "missing.md"])
        require(code == 2 and report["read_errors"], "missing file must be a read error")
    return len(samples)


def main():
    count = 0
    for locale, name in (("en", "concept-design"), ("zh-CN", "concept-design-cn")):
        count += check_package(ROOT / "skills" / locale / name)
    print(f"OK: single concept entry pair, {count} packaged syntax examples, negative cases, and read-only checks")


if __name__ == "__main__":
    main()
