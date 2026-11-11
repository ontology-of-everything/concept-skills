# Execution, recovery, and migration

This document defines engineering execution requirements. Specify business behavior using the [specification notation](spec-notation.md); add applicable runtime requirements without repeating action or synchronization definitions.

## Execution constraints

Record a concept's own execution requirements in `CONCEPT.md` and cross-concept requirements in `SYNCS.md`.
Append execution requirements where needed; a separate section is not required in every specification.
Reference existing action contracts and the [execution checks](#execution-checks); record the model's assumptions and policies without copying those definitions.
Cover completion, concurrency/order, correlation and repetition, failure effects, and required timing, retries, and recovery as applicable.
Record confirmed policies; mark unresolved items `open` and irrelevant items `not applicable`.
Execution requirements MUST state permitted observable behavior, required outcomes, and their assumptions.
Each requirement MUST identify its action contract or rule and acceptance checks.
Execution evidence MUST link actual effects to action occurrences, causal origins, and the applicable specification.

## Execution checks

- An invocation requests execution; a completion records its result.
  Occurrence identity connects them; equal arguments do not.
  Asynchronous actions MUST define when they complete.
  Acceptance or enqueue completion does not complete subsequent work.
- A flow contains a root occurrence and its causal descendants.
  Calls emitted by `then` and their completions MUST retain the triggering flow.
  Repeated actions need occurrence/cause correlation as well as request/business identity.
  Specify all matches or a particular attempt.
  `// flow:` only labels documentation.
- Old completions from independent flows MUST NOT satisfy `when`.
  Use `where` for persistent facts and an entry/correlation protocol for delayed callbacks.
- Match errors separately from values such as `valid: false`.
  Runtime exceptions handled by rules MUST map to declared result cases.
  Required access checks MUST precede protected effects.
  Later refusal does not undo writes.
- Zero rows emit no calls; multiple rows expand calls.
  Specify required zero-match responses and candidate selection.
- Later failures MUST NOT erase existing completion records.
  Define responses, retries, compensation, or intentional ignore and their effects.
- Verify firing identity and atomic deduplication for occurrence tuples and rows.
  Reevaluation MUST preserve legitimate repetitions and prevent forbidden duplicates.
- In-memory records MAY suffice without restart recovery.
  Required recovery MUST preserve pending work and causal correlation; use the [recovery protocol](execution.md#atomicity-and-recovery).
  External effects need separate idempotency.

## Rule execution

Implement named rules as functions or objects in composition.
Choose storage from the declared durability and recovery requirements.
Atomically claim each matched completion tuple and binding row before emitting calls.
Ordinary calls, listeners, and Promise chains need the same guarantees.

Implement the declared outcome policies, request correlation, candidate selection, and loop controls from the owning SYNCS.
Later-valid query results need an explicit reevaluation trigger.
When reevaluating the same completion, declare whether new bindings may emit calls and define firing identity accordingly.
Enforce invariant checks atomically inside the action; preserve the required consistency between authorization and protected effects.

## Atomicity and recovery

A database transaction does not make an external effect atomic.
Use cross-concept transactions only if contracts permit them and stores can participate.

When restart recovery is required:

1. Commit business state atomically with the completion/outbox record that drives later work, or define explicit reconciliation.
   A crash between state commit and completion recording MUST NOT silently lose required work.
2. Before dispatch, atomically record the firing claim and pending calls.
   Retain completion identities, flow, rule identity/version, bindings, and causes needed for replay.
3. Handle a crash after target commit but before acknowledgement.
   Use stable invocation identity and receiver deduplication, or declared reconciliation.
   A processed-match marker alone does not guarantee exactly-once effects.
4. Apply equivalent idempotency checks to external effects.
   Later failure MUST NOT erase completed actions.
   Compensation need not restore the original state.
5. Bound retries or define controlled continuation, and expose exhaustion.

The [external login example](spec-examples.md#external-identity-login) illustrates partial effects: an error response does not undo completed identity or profile changes.

## Compatibility

Changes to state, identities, interfaces, or rules require inspection of stored data, deployed callers, pending calls, and historical completions.
Define applicable migration, backfill, old/new compatibility, and rollback or roll-forward before applying the change.
Version rules or drain affected work when replay would reinterpret old completions.
A code rename does not authorize a stored-identity change.
For code-only moves, verify whether migration is unnecessary rather than adding machinery by default.

## Checks

Run applicable cases: success/refusal, zero/many bindings, repeated equal-valued actions, cross-flow completions, concurrent duplicate evaluation, state change
between query and write, crash before publication, crash before acknowledgement, redelivery, in-flight migration, and retry exhaustion.
Link executed checks to their contracts.
