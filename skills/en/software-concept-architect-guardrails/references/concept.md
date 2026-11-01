# Concept specification

Use [the contract](spec-format.md) to create a confirmed specification or backfill one from code.

## Establish the boundary

A purpose states one need; state/actions define allowed behavior; the operational principle explains
a useful result. The definition assumes no other concept's fields. Use type parameters for external
identities, SYNCS for coordination, and notes for application context.

Writes go through declared actions; reads use public abstract state or queries. Concepts neither
call one another nor share mutable state. An action declares allowed behavior; a completion records
an occurrence. Events, logs, and metrics alone do not establish a concept.

## Write from evidence

Inspect exports, callers, persistence, failures, invariants, and tests. Separate facts, inferred
purpose, defects, and open decisions. An idealized OP must not justify defective code.
Check how actions produce the OP result and how that result meets the need; report counterexamples.

Write confirmed types, cardinality, initial state, actions/results, and queries where applicable.
Private helpers/caches need no contract entry without observable effect. Preserve gaps rather than
inventing behavior. Discovery only lists candidates. Keep one CONCEPT, colocate its PIPELINE, and
update the index. Identify required syncs without embedding them. Record coupling in decisions or
drift reports, not legacy interactions/dependencies sections. Complex model choices go to design.
