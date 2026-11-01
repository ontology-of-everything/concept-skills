# Reservation design example

This teaching fragment follows [the contract](spec-format.md) and is not a complete product. Open behavior
must be defined before implementing the affected part.

## Independent concepts

```text
# concept Reserving [U, S]
## purpose
Commit a resource slot to a user for future use.
## state
reservations: set Reservation
user: Reservation -> U
slot: Reservation -> S
status: Reservation -> Status
Reservation is a local identity. Status = booked | canceled | granted.
Initially reservations is empty. Each reservation has one user, slot, and status.
Each S has at most one booked reservation. Assume no fields on S.
## actions
reserve [user: U; slot: S] => [reservation: Reservation]
  requires slot has no booked reservation
  ensures creates a booked reservation and returns its identity; other state is unchanged
reserve [user: U; slot: S] => [error: Conflict]
  requires slot already has a booked reservation
  ensures returns Conflict and leaves state unchanged
cancel [reservation: Reservation] => []
  requires reservation is booked
  ensures changes only its status to canceled
grant [reservation: Reservation] => []
  requires reservation is booked; arrival conditions remain open
  ensures changes only its status to granted
## operational principle
after reserve [user: u; slot: s] => [reservation: r]
then, if not canceled and arrival conditions hold, grant [reservation: r] => [] fulfills the commitment.
```

Arrival inputs/timing and out-of-precondition cancel/grant handling remain open. Do not invent errors.
Purpose fulfillment depends on defining and checking arrival.

```text
# concept Availability [V]
## purpose
Let users find resource slots currently offered at a venue.
## state
slots: set Slot
venue: Slot -> V
offered: set Slot
Slot is a local identity. Initially slots and offered are empty.
Each Slot has one V; offered is a subset of slots.
## actions
publish [venue: V] => [slot: Slot]
  requires true
  ensures creates a Slot, associates it with venue, and adds it to offered; other state is unchanged
withdraw [slot: Slot] => []
  requires slot belongs to slots
  ensures removes slot from offered; other state is unchanged
## operational principle
after publish [venue: v] => [slot: s]
then s is offered with venue(s)=v; after withdraw [slot: s] => [], offered-slot queries omit s.
## queries
_find [venue: V] => [slot: Slot]
  returns every offered slot for venue, one per row; no match returns an empty set
```

The query reads venue/offered without producing a completion; Availability never reads Reserving.
Handling an unknown Slot remains open.

## Application scenario

After selecting one slot, the user receives a reservation or conflict. Arrival is outside this
fragment. The application supplies UserId, VenueId, and RequestId:

```text
Requesting/reserve: [user: UserId; slot: Availability.Slot] => [request: RequestId]
Requesting/respond: [request: RequestId; reservation: Reserving.Reservation] => []
Requesting/respond: [request: RequestId; error: Conflict] => []
```

RequestId identifies this request; Conflict is Reserving's declared error. Request completion starts
one flow inherited by later calls.

```text
# app Reservations
include Availability [VenueId]
include Reserving [UserId, Availability.Slot]
include Requesting

// flow: reserve
sync reserve
when {
  Requesting/reserve: [user: ?user; slot: ?slot] => [request: ?request]
}
then {
  Reserving/reserve: [user: ?user; slot: ?slot]
}

sync accepted
when {
  Requesting/reserve: [user: ?user; slot: ?slot] => [request: ?request]
  Reserving/reserve: [user: ?user; slot: ?slot] => [reservation: ?reservation]
}
then {
  Requesting/respond: [request: ?request; reservation: ?reservation]
}

sync rejected
when {
  Requesting/reserve: [user: ?user; slot: ?slot] => [request: ?request]
  Reserving/reserve: [user: ?user; slot: ?slot] => [error: ?error]
}
then {
  Requesting/respond: [request: ?request; error: ?error]
}
```

Accepted/rejected match output fields and the same user/slot in one request. They do not wait for
_find. An empty query is not an error, and multiple candidates do not authorize booking all.
Offered state may change before writing; withdrawal/reservation concurrency remains open.

## Diagram and subsets

Reserve connects request completion to Reserving.reserve. Accepted/rejected each require both
completions before responding. Draw query reads separately from triggers.

A product accepting known slot identities may need only Reserving. Required discovery justifies the
product dependency on Availability; type instantiation alone does not.

Authentication, venue checks, concurrent withdrawal, display, arrival, cancellation entries, and
fault handling remain open. The rules cover only a selected slot's success or conflict.
