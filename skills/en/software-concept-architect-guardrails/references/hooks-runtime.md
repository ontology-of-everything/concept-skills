# Optional hooks runtime

Enable only on request, with Claude Code, bash, and jq. Retain wyx v0.26.0 scripts and MIT notices.
Specification work itself does not require these hooks.

| Hook | Behavior |
| --- | --- |
| SessionStart | Lists specifications, last history snapshot, mtime hints, shadowing warnings, and a missing-jq warning. |
| PreToolUse | Finds the nearest CONCEPT/PIPELINE before Write/Edit/NotebookEdit; injects PIPELINE data boundary only. |
| PostToolUse | Looks for legacy CONCEPT dependencies; silent with this notation. |

The nearest CONCEPT/PIPELINE ends boundary lookup. SYNCS is listed, not parsed. A PIPELINE-only
folder may trigger an ancestor lookup and SHADOWED warning. Root selection uses CLAUDE_PROJECT_DIR,
input cwd, then current directory; an empty or filesystem root stops scanning. The extractor handles
limited headings, skips json/jsonl/lock/log/txt, and prompts for specification edits.

Hooks do not block writes or check imports, contracts, or rules. Bash/MCP writes and other clients
are not automatically covered. Read local specifications; do not add legacy sections to satisfy a hint.

Inspect `runtime/hooks/hooks.json` and all three runtime scripts. Preserve existing settings when installing the plugin or
merging hooks into `.claude/settings.json`; replace CLAUDE_PLUGIN_ROOT with an absolute path.
Run `bash -n` and parse JSON before activation. Start a new session, confirm each hook
fires once, and test unrelated work. Removal restores previous settings and removes only installed files.

History is opt-in under [drift](drift-detection.md#report-and-optional-history). SessionStart reads the
last snapshot, with specs_remaining for fix records. Scoped results and mtime do not prove whole-project
freshness. The runtime has no check-rules.sh; validation lives in repository QA.
