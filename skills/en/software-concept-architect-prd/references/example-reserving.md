# Reservation transcription example

Transcribe this confirmed fragment; do not treat it as a complete product or fill omitted fields.

## Confirmed input and location

Reserving commits slots; Availability offers them. Reserve returns reservation or Conflict without
state change on collision. _find returns all offered slots for a venue, with an empty set for none.

The user selects one slot. Requesting/reserve takes user/slot and returns request; respond takes
request plus reservation or error and returns no fields. The application provides UserId, VenueId,
and RequestId; Conflict is Reserving's error. Correlate flow/request and user/slot.

| Content | Existing module | Before module creation |
| --- | --- | --- |
| Concept's four sections | Module's CONCEPT.md | docs/prd/concepts/ |
| Instances and rules | composition/SYNCS.md | docs/prd/SYNCS.md |
| Needs, dependencies, diagram, open decisions | docs/prd/README.md | Same |

Keep local parameters in CONCEPT and actual type instantiation in SYNCS.

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

## Acceptance and gaps

Trace a fulfillable commitment to reserve/grant, retaining arrival assumptions. Missing grant or
arrival contracts leave acceptance incomplete. Trace unchanged-state collision to the reserve error case.

Do not convert empty _find results into undeclared errors or candidates into bookings for all.
Keep identity, concurrency, arrival, and cancellation gaps until confirmed. Verify unique file
ownership, valid indexes, conjunctive accepted/rejected triggers, and query reads distinct from completions.
