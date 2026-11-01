# Specification coverage audit

Run audit read-only. Read project conventions, PRD/staged indexes, specifications, code entries,
state/schema/migrations, tests, build manifests, and existing maps within scope. Skip dependency and
generated/build trees, but inspect single-file core modules too.

## Classify evidence

For each module or flow, record one status: covered, staged, missing, support code, or unverified.
Name the authoritative file and actual coverage, or explain the missing evidence/skip reason.
An ancestor file covers a module only when its content does.

Build units and concepts are different. Concepts need independent purpose and coherent behavior;
composition rules belong in SYNCS, data transformations in PIPELINE, and protocol/wiring/types may
need neither. Tables, classes, logs, queues, imports, and file counts are only search clues.
Report direct concept calls as coupling, even through public interfaces.

## Report and plan

Return scope, counts, candidates with locations, broken links, and migration work. Do not report a
coverage percentage without enumerating its denominator. Coverage proves neither fitness nor correctness.

Order backfill commands by actual code dependencies, handling cycles together and marking boundary
problems. Code dependencies determine this order, not product dependencies. Each command states mode,
path, evidence, expected artifact, and prerequisite; sort paths within a batch. Execute no repairs.
Send freshness checks to drift, maps to map, and purpose/conformance review to review.
