# Execution, recovery, and migration

Use [the shared contract](../spec-format.md) for matching, bindings, results, and correlation.

## Rule execution

Implement named rules as functions or objects in composition.
In-memory records suffice unless restart recovery is required.
Atomically claim each matched completion tuple and binding row before emitting calls.
Repeated evaluation MUST neither duplicate a forbidden effect nor suppress a legitimate repeated action.
Ordinary calls, listeners, and Promise chains need the same guarantees.

For each reachable result, implement the declared response, retry, compensation, or intentional-ignore policy and state consequences.
Required responses MUST cover refusal and zero matches without omission, duplication, or delivery to another request.
Define candidate selection before choosing one or acting on all.
Later-valid query results need an explicit reevaluation trigger.
Check business permissions before the protected effect under the required consistency policy.
A prior query cannot replace an action's atomic invariant check.
Loops MUST terminate or have controlled continuation.

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

For a confirmed policy that releases a reservation after payment declines, a temporary release failure leaves release work pending.
Retrying release MUST NOT charge again.

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
