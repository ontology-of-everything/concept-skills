#!/usr/bin/env python3
"""Reject Git-ignored files in a worktree, proposed commit, or outgoing history."""
import argparse
import os
from pathlib import Path
import subprocess
import sys


def git(root, *args, data=None, check=True):
    result = subprocess.run(["git", "-C", str(root), *args], input=data, capture_output=True)
    if check and result.returncode:
        raise RuntimeError(result.stderr.decode(errors="replace").strip())
    return result


def ignored(root, files):
    if not files:
        return set()
    data = b"\0".join(os.fsencode(p) for p in files) + b"\0"
    result = git(root, "check-ignore", "--no-index", "-z", "--stdin", data=data, check=False)
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stderr.decode(errors="replace").strip())
    return {os.fsdecode(p) for p in result.stdout.split(b"\0") if p}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Git worktree to inspect")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--staged", action="store_true", help="Inspect the complete proposed index")
    modes.add_argument("--revision", help="Inspect one committed tree")
    modes.add_argument("--pre-push", action="store_true", help="Inspect outgoing commits from hook stdin")
    args = parser.parse_args()
    root = Path(os.fsdecode(git(args.repo, "rev-parse", "--show-toplevel").stdout).strip())
    revisions = set()
    if args.pre_push:
        for line in sys.stdin:
            _, local, _, remote = line.split()
            if set(local) == {"0"}:
                continue
            rev_args = [local]
            if set(remote) != {"0"} and git(root, "cat-file", "-e", remote, check=False).returncode == 0:
                rev_args.append("^" + remote)
            revisions.update(git(root, "rev-list", *rev_args).stdout.decode().splitlines())
    elif args.revision:
        revisions.add(args.revision)
    violations = set()
    if args.pre_push or args.revision:
        for revision in revisions:
            paths = git(root, "ls-tree", "-r", "--name-only", "-z", revision).stdout
            violations.update(ignored(root, [os.fsdecode(p) for p in paths.split(b"\0") if p]))
    else:
        paths = git(root, "ls-files", "--cached", "-z").stdout
        files = [os.fsdecode(p) for p in paths.split(b"\0") if p]
        if not args.staged:
            files = [p for p in files if (root / p).exists() or (root / p).is_symlink()]
        violations.update(ignored(root, files))
    if violations:
        print("FAIL: local-only files must not be committed or pushed:", file=sys.stderr)
        for path in sorted(violations):
            print("  " + path, file=sys.stderr)
        return 1
    print("OK: repository hygiene passed" + (f" ({len(revisions)} outgoing/selected commits)" if revisions else ""))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
