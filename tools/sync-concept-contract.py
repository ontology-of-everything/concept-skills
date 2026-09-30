#!/usr/bin/env python3
"""Keep standalone concept skill packages on one maintained spec contract."""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="refresh packaged copies")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    stale = []
    for locale, suffix in (("en", ""), ("cn", "-cn")):
        source = root / "skills" / locale / f"software-concept-architect-design{suffix}" / "references/spec-format.md"
        content = source.read_bytes()
        for name in ("software-concept-architect-prd", "software-concept-architect-build", "software-concept-architect-review", "software-concept-architect-guardrails"):
            target = root / "skills" / locale / f"{name}{suffix}" / "references/spec-format.md"
            if args.write:
                target.write_bytes(content)
            elif not target.exists() or target.read_bytes() != content:
                stale.append(str(target.relative_to(root)))
    if stale:
        parser.exit(1, "Stale contract copies; run tools/sync-concept-contract.py --write:\n" + "\n".join(stale) + "\n")
    print("OK: concept specification contract copies are consistent")


if __name__ == "__main__":
    main()
