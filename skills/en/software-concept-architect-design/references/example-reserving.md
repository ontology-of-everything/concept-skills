# Reservation Transcription Example

This example shows authoritative placement and traceability for a confirmed Reserving/Availability
fragment; it is neither paper text nor a complete product.

## Confirmed Input

- Reserving [U, S] maintains reservation commitments; Availability [V] provides slots.
- `Reserving.reserve` returns `reservation` on success and `Conflict` without state change on
  collision.
- `Availability._find` returns every offered slot for one venue; an empty set means no candidate.
- After the user chooses one slot, `Requesting/reserve` receives named user/slot fields and returns
  `request`; `Requesting/respond` receives request plus reservation or error and returns no fields.
- The application supplies UserId, VenueId, and RequestId. Correlate responses by flow/request and
  user/slot.

Place each concept's four sections beside its module or under `docs/prd/concepts/`, application
instantiation and rules in `syncs/SYNCS.md` or staged `docs/prd/SYNCS.md`, and user needs,
dependencies, graph, and open decisions in `docs/prd/README.md`. Keep local type parameters inside
CONCEPT and concrete instantiation inside SYNCS.

```text
# app Reservations
include Availability [VenueId]
include Reserving [UserId, Availability.Slot]
include Requesting

// flow: reserve
sync reserve
when { Requesting/reserve: [user: ?user; slot: ?slot] => [request: ?request] }
then { Reserving/reserve: [user: ?user; slot: ?slot] }

sync accepted
when {
  Requesting/reserve: [user: ?user; slot: ?slot] => [request: ?request]
  Reserving/reserve: [user: ?user; slot: ?slot] => [reservation: ?reservation]
}
then { Requesting/respond: [request: ?request; reservation: ?reservation] }

sync rejected
when {
  Requesting/reserve: [user: ?user; slot: ?slot] => [request: ?request]
  Reserving/reserve: [user: ?user; slot: ?slot] => [error: ?error]
}
then { Requesting/respond: [request: ?request; error: ?error] }
```

Trace “a successful reservation creates a fulfillable commitment” to the reserve/grant contracts and
preserve attendance assumptions. If grant or attendance is missing, mark acceptance incomplete.
Trace collision with unchanged state to the reserve error case.

Never turn `_find` empty results into an undeclared error or multiple candidates into reservations
for all. Keep identity, concurrency, attendance, and cancellation open until confirmed. Verify one
location per element, valid indexes, conjunctive accepted/rejected graph edges, and queries not
drawn as completions.
