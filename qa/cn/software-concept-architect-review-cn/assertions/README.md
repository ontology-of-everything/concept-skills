# Assertions

Evaluate observable audit behavior rather than exact headings or wording.

- The skill runs only on explicit `$software-concept-architect-review-cn` / `/software-concept-architect-review-cn` invocation.
- The run stays read-only: no files are created or edited.
- All five dimensions run, or skipped dimensions are named with a reason.
- Each finding has a location, evidence a reviewer can re-check, a severity,
  and exactly one routing target.
- Related findings collapse to a root cause when they share one model or code
  defect.
- Repair routing follows the current root cause; dependent repairs are sequenced.
- Model-only audits do not invent implementation evidence or report absent-code
  test coverage as a defect.

- Concept purposes and application purposes are distinguished; local OP success
  does not establish fitness of the application composition.
- Definitions, meaningful relations and evidence guide decisions; checklist
  completion alone does not establish design correctness.
