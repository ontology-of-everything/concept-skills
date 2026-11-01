# Execution and recovery

Implement [the contract's](spec-format.md) completion matching, bindings, result cases, and correlation.
State changes alone do not trigger rules, and calls within one then group have no implicit order.

## Choose an implementation

Keep rules named and connect them through concept actions, not direct rule calls.
Use a mediator for simple coordination. Consider an engine when joint matching, historical
correlation, or recovery makes manual scheduling difficult. Verify its installed capabilities;
listeners and Promise chains alone do not provide these guarantees.

## Requests and results

Preserve flow, business-object, and request identity so repeated actions and concurrent requests
cannot match incorrectly. Documentation groups provide no runtime identity.
Distinguish successful results, declared errors, and negative values such as `valid: false`.
Honor public-interface permissions and obtain authorization before writing.

Every reachable result needs the entry contract's response, retry, compensation, or intentional-ignore
strategy and state consequences. Required responses cover refusal and zero matches without loss,
duplication, or cross-request delivery. Multiple candidates do not authorize taking the first or all.

## Atomicity and recovery

Actions enforce their own invariants atomically; an earlier query cannot replace the write-time check.
A database transaction does not make an external effect atomic. Cross-concept transactions require
contract permission, participating stores, and isolated external effects.

When recovery is required, persist completions, matched rules/bindings, pending calls, and causal links.
Deduplicate matched occurrences under the engine contract. Publish completions after commit or through
a consistent outbox. External effects need separate idempotency. A later failure does not erase
completed actions, and compensation need not restore the original state.

Loops need termination, a retry budget, or controlled continuation. Expose exhausted retries and cutoffs.

## Example and checks

If payment is declined after a reservation is held, release the hold. A temporary release failure
leaves pending work to retry without charging again. Report the actual pending/failed status.

Check rule cases and bindings, concurrent isolation, restart after partial completion, redelivery,
and retry exhaustion. Link each check to its contract.
