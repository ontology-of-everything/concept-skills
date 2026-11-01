# Specification layout

Use [the contract](spec-format.md) for syntax and [the reservation example](example-reserving.md)
for transcription. Each model element has one authoritative location.

| Content | Location and required links |
| --- | --- |
| Purpose, scenarios, counterexamples, assumptions | Overall PRD; retain evidence for concept and rule choices. Missing goals stay open. |
| One concept | CONCEPT.md beside its module, or staged under `docs/prd/concepts/`; retain four core sections, declared queries, and notes. |
| Application composition | Composition module's SYNCS.md, or staged `docs/prd/SYNCS.md`; include app/type bindings, external-entry signatures, and rules grouped by `// flow:`. |
| Acceptance | Overall PRD or existing acceptance file; cite an OP, action case, invariant, or application scenario. |
| Diagrams, dependencies, exclusions, open decisions | Overall PRD; derive sync diagrams from rules and justify product dependencies from requirements. |

Preserve confirmed signatures, results, state meanings, and human notes. Resolve referenced types,
actions, and queries. Omit `[]` when a concept has no type parameters; actions with no result use `=> []`.

During implementation, colocate one CONCEPT per concept build unit and one SYNCS per composition
unit. Flow groups need no extra specifications. Update indexes after moving staged files or splitting
real modules. For legacy migration, recover result cases, correlation, and state effects before
changing notation; do not turn ambiguity into a requirement.
