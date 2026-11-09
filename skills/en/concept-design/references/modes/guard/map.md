# Concept and Synchronization Diagram

Generate one `ARCHITECTURE.md` with a Mermaid diagram from local CONCEPT and SYNCS files.
Version 1 excludes PIPELINE, PRD, and source code.

```sh
python3 <skill-directory>/scripts/concept_map.py <root> --output <root>/ARCHITECTURE.md
```

Use `--scope RELPATH` for selected definitions and rules with their direct instance boundaries.
Repeat `--exclude PATTERN` to omit paths.
Omit `--output` to print Markdown to stdout.
`--check` requires `--output` and compares without writing.

When checking identity, resolution, or output rules, consult [the map format](../../shared/artifacts/map-format.md).
Report output path or stdout, scope, exit status, and gaps.
A partial diagram may be written but MUST be marked partial.
With no specifications, existing output MUST remain unchanged.
The diagram maps specification references; it is not Jackson's purpose-dependency graph.
It establishes neither code coverage nor runtime correctness.
