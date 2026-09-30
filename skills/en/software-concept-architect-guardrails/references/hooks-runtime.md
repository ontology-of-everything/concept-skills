# Optional Hooks Runtime

The bundled Claude Code hooks surface relevant specifications at session start, warn when edited
files may make derived maps stale, and inject a PIPELINE data-boundary reminder before applicable
tools. They improve visibility but do not validate semantic seams, prove freshness, or replace CI.

Enable only when the user requests hook installation and the project supports Claude Code hooks and
`jq`. Inspect `runtime/hooks/hooks.json` and the three scripts before copying. Preserve existing
hooks and merge registrations rather than overwriting them. Run `bash -n` on scripts and parse both
JSON files before activation.

After installation, start a clean session and verify SessionStart, PreToolUse, and PostToolUse each
fire once without blocking unrelated work. Removal restores the previous hook configuration and
deletes only files installed by this skill.
