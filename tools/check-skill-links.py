#!/usr/bin/env python3
"""Check literal local Markdown links and entry-point resource paths in skill packages."""

from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


LINK = re.compile(r"\[[^\]\n]+\]\(([^\s()]+)(?:\s+\"[^\"]*\")?\)")
RESOURCE = re.compile(r"`((?:references|assets|runtime)/[^`\s]+)`")


def prose(text):
    """Exclude fenced examples, whose links need not refer to the install payload."""
    fence = None
    for line in text.splitlines():
        marker = re.match(r"^\s*(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            yield line


def check_package(package):
    package = package.resolve()
    errors = []
    for source in sorted(package.rglob("*.md")):
        for line in prose(source.read_text(encoding="utf-8")):
            references = [(value, source.parent) for value in LINK.findall(re.sub(r"`+[^`]*`+", "", line))]
            if source.name == "SKILL.md":
                references += [(value, package) for value in RESOURCE.findall(line)]
            for value, base in references:
                parsed = urlsplit(value.strip("<>"))
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                target = (base / unquote(parsed.path)).resolve()
                if not target.is_relative_to(package):
                    errors.append(f"{source.relative_to(package)}: link escapes package: {value}")
                elif not target.exists():
                    errors.append(f"{source.relative_to(package)}: missing local resource: {value}")
    return sorted(set(errors))


def main():
    root = Path(__file__).resolve().parents[1]
    packages = sorted((root / "skills").glob("*/*/SKILL.md"))
    errors = [f"{entry.parent.relative_to(root)}: {error}"
              for entry in packages for error in check_package(entry.parent)]
    if errors:
        raise SystemExit("FAIL: local skill links\n" + "\n".join(errors))
    print(f"OK: literal local links and entry resources resolve in {len(packages)} skill packages")


if __name__ == "__main__":
    main()
