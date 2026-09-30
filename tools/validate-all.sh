#!/usr/bin/env bash
# Traverse qa/<locale>/<skill>/validate.sh, matching the GitHub workflow.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
status=0

python3 "$ROOT/tools/validate-localization.py"
python3 "$ROOT/tools/skill-catalog.py"

while IFS= read -r validate; do
  name=$(basename "$(dirname "$validate")")
  printf '==> %s\n' "$name"
  if ! "$validate"; then
    status=1
  fi
  printf '\n'
done < <(find "$ROOT/qa" -mindepth 3 -maxdepth 3 -name validate.sh -type f | sort)

[[ "$status" -eq 0 ]] || exit "$status"
printf 'OK: all skill QA passed\n'
