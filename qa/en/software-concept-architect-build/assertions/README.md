# Assertions

Evaluate observable mapping behavior rather than exact folder names.

- The skill runs only on explicit `$software-concept-architect-build` /
  `/software-concept-architect-build` invocation.
- Each concept, syncs, gateway, and shared module has a build/test unit and a bounded
  public API. They run in one process; concepts do not import each other.
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

- Gateway calls syncs APIs; server may assemble modules through public entries.
- Internal dependencies point toward domain/application contracts; no empty layers
  or forwarding-only wrappers are required.
- Build graphs and source/API checks are distinct; independent builds include declared
  dependencies and do not imply separate deployment.
- Existing confirmed architectures are assessed on their own terms; single-module
  requests do not trigger unrelated application scaffolding.
