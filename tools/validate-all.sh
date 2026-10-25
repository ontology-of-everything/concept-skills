#!/usr/bin/env bash
# Public checks work in a clean checkout; private QA is an explicit local option.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONDONTWRITEBYTECODE=1
[[ $# -eq 0 || ( $# -eq 1 && $1 == --local-qa ) ]] || {
  printf 'Usage: %s [--local-qa]\n' "$0" >&2; exit 2;
}
python3 "$ROOT/tools/check-repository-hygiene.py" --repo "$ROOT"
python3 "$ROOT/tools/validate-localization.py"
python3 "$ROOT/tools/skill-catalog.py"
python3 "$ROOT/tools/sync-concept-contract.py"
if [[ ${1:-} == --local-qa ]]; then
  count=0 status=0
  for validate in "$ROOT"/qa/{en,cn}/*/validate.sh; do
    [[ -f "$validate" ]] || continue
    count=$((count + 1))
    "$validate" || status=1
  done
  [[ $count -gt 0 ]] || { printf 'FAIL: local QA is unavailable\n' >&2; exit 1; }
  [[ $status -eq 0 ]] || exit "$status"
fi
printf 'OK: public skill checks passed\n'
