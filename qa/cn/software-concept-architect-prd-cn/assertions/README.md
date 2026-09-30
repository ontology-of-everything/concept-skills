# Assertions

Evaluate observable PRD-transcription behavior rather than exact headings.

- The skill runs only on explicit `$software-concept-architect-prd-cn` / `/software-concept-architect-prd-cn` invocation.
- The skill transcribes a confirmed model; it does not invent concepts, syncs,
  or exclusions.
- Model gaps route back to `software-concept-architect-design` instead of being filled in
  the documents.
- Each concept gets its own sub-PRD that does not depend on other concept definitions; same-named local parameters are valid.
- Syncs are grouped by flow, not by domain directory.
- Acceptance scenarios trace to concept OPs, application scenarios or action/state contracts; no code is written.

- Concept purposes and application purposes are distinguished; local OP success
  does not establish fitness of the application composition.
- Definitions, meaningful relations and evidence guide decisions; checklist
  completion alone does not establish design correctness.
