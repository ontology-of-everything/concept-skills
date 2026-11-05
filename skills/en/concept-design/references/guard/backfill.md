# Reconstruct specifications

Inspect actual code and write an evidenced candidate baseline using [the format](../spec-format.md).
Label each claim's evidence and confirmation status.
MUST separate observed behavior, inferred purpose, known defects, desired repairs, and confirmed requirements.
State which consumers may rely on the reconstructed contract.
Record evidenced [execution constraints](../spec-format.md#execution-constraints); unknown policies remain open.

## Concept

Inspect exports, callers, persistence, result cases, invariants, and tests.
Write evidenced types, cardinality, initial state, actions/results, and applicable queries.
Private helpers/caches need no entry without observable effects.
List required syncs separately.
Record coupling as an observed defect in decisions/drift, not as a permitted concept dependency.

## Synchronization

Start from application purpose/scenarios and trace handlers, registrations, mediators, and adapters to public actions.
Transcribing direct concept calls/private SQL does not make them valid rules.
Pure data transformation belongs in [PIPELINE](pipeline.md).
Resolve entry completions, result cases, bindings, calls, response obligations, occurrence/object/request correlation, partial completion, replay, and loops.
All groups reference one application-level instance/type/entry declaration; repeated includes MUST NOT create per-file instances.
Use [architecture naming/ownership](../engineering/architecture.md) when mapping code.

Check all includes, signatures, and call arguments.
Preserve zero/many query behavior and request isolation.
Each reachable result needs its declared response/retry/compensation/ignore policy.
Loops terminate or continue under explicit control; a depth cap is optional.
Diagrams preserve conjunctions, multiple targets, and query reads.
Report rule count, scenario coverage, boundary findings, and unknowns.
