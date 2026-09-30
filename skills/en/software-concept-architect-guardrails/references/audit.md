# Specification Coverage Audit

Use `audit` for read-only discovery before creating or changing specifications. Inspect project
instructions, the overall PRD, CONCEPT/SYNCS/PIPELINE files, implementation modules, entry points,
tests, schemas, migrations, build boundaries, and generated maps.

## Classify

For every module or flow, record one state:

- covered by an authoritative specification with a valid index link;
- staged because the target module does not yet exist;
- missing despite evidenced concept behavior or coordination;
- not a concept/synchronization/pipeline, with the observed reason;
- unverified because required material could not be read.

Distinguish facts from inferred purpose and open design. Do not infer a concept merely from a table,
class, route, service, log, or queue. A candidate needs an independent purpose and coherent
behavior.

## Plan and Completion

Return scan scope, coverage counts, candidates, broken references, and a dependency-ordered command
plan. Each command names the mode, path, evidence, expected artifact, and prerequisite. Do not
execute repair in audit mode. Complete only after every scanned candidate has a state and every
declared specification/index link has been checked.
