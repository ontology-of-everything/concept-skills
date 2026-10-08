# Drift Detection

Use `drift` read-only. Compare every specification with current implementation, schema/migrations,
tests, overall indexes, and derived maps. Treat format compatibility separately from semantic drift.

## Evidence

Trace public entry points, actions and queries, state ownership, persistence, error cases,
synchronizations, pipeline stages, and dependency rules. Search results are leads; open the defining
code before concluding. Mark unscanned or generated paths unverified.

Check manifests and source dependencies against confirmed engineering conventions. For the modular
monolith baseline, verify independent build units, public APIs, gateway → syncs → concepts, zero
concept dependencies, and Clean Architecture layers. Allow public assembly entries for server.
Report architectural deviations separately; defaults do not establish legacy-project violations,
and folders or acyclicity are not sufficient boundary evidence.

For CONCEPT, check missing/removed actions, changed signatures or cases, observable undeclared
state, broken invariants, OP test gaps, and cross-concept access. For PIPELINE, check sources, stage
order, schemas, outputs, triggers, invariants, and data boundaries. For SYNCS, check includes,
completion triggers, success/error patterns, `where` cardinality, `then` arguments, participants,
correlation, failure, replay, and loops. Resolve every cross-spec action and query.

Report each finding with severity, specification location, implementation evidence, behavioral
impact, and repair route. Keep omissions distinct from contradictions and merge symptoms sharing one
root cause. Add history only when requested; never modify code or specifications in drift mode.
