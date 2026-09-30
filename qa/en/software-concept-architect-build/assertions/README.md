# Assertions

Evaluate observable mapping behavior rather than exact folder names.

- The skill runs only on explicit `$software-concept-architect-build` /
  `/software-concept-architect-build` invocation.
- Each concept has a verifiable module boundary; concept modules do not import each
  other.
- Syncs land only in the composition layer (mediator or rule engine).
- Language-specific notes are loaded only for the requested language.
- Concept-boundary questions route back to `software-concept-architect-design`; the skill
  does not reopen modeling.
- Architecture-guard tests are part of the done criteria, not an optional
  afterthought.

- Concept purposes and application purposes are distinguished; local OP success
  does not establish fitness of the application composition.
- Definitions, meaningful relations and evidence guide decisions; checklist
  completion alone does not establish design correctness.
