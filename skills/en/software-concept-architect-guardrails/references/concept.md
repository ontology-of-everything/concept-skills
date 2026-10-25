# Concept Specification

Use `concept` to create a confirmed concept specification or backfill an evidenced contract from
implementation. Read `spec-format.md` first.

- Purpose states one evaluable need; the OP uses a discriminating scenario to show fulfillment;
  state and actions define allowed behavior.
- Core sections remain independent of other concept definitions. Type parameters express identity
  without field assumptions. Cross-concept business behavior belongs in SYNCS; notes hold
  application context.
- State ownership defines the seam: writes use declared actions, reads use public abstract state or
  declared queries, concepts neither call one another nor share mutable state.
- An action declaration says what may occur; a completion records what did occur. Logging or metrics
  are not concepts without independent purpose and behavior.

## Work

For creation, derive purpose, OP, state, actions, cases, and assumptions from confirmed design. For
backfill, trace public entry points, persistence, invariants, errors, and tests; label observed
facts, inferred purpose, current defects, and open decisions. Never use an idealized OP to justify
defective behavior.

Write one authoritative CONCEPT file, update the overall index, and identify required
synchronizations without embedding them. Completion requires named types, cardinality and
initial-state facts where needed, complete observable action cases, an evidenced purpose argument,
and resolvable links.
