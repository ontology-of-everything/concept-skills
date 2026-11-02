# Complete concept and partial composition

These are teaching choices, not requirements for other products.
Use the [specification format](spec-format.md).

## Complete Todo

A trusted local caller remembers unfinished work.
Text is any string, including empty text.
Task identities are fresh and never reused.
Deletion, ordering, authorization, and durability are outside this example.

```text
# concept Todo
coverage: complete
## purpose
Remember unfinished work and distinguish it from completed work.
## state
tasks: set Task
text: Task -> Text
done: set Task
Task is a local identity; Text is a string.
Initially tasks and done are empty.
text has domain exactly tasks, with one Text per task; done is a subset of tasks.
Missing is the singleton error for an unknown task.
## actions
add [text: Text] => [task: Task]
  requires true
  ensures creates and returns one fresh t; tasks = old tasks union {t};
          text = old text plus (t, input text); done is unchanged
complete [task: Task] => []
  requires task belongs to tasks
  ensures done = old done union {task}; other state is unchanged
complete [task: Task] => [error: Missing]
  requires task does not belong to tasks
  ensures returns Missing; state is unchanged
reopen [task: Task] => []
  requires task belongs to tasks
  ensures done = old done minus {task}; other state is unchanged
reopen [task: Task] => [error: Missing]
  requires task does not belong to tasks
  ensures returns Missing; state is unchanged
## operational principle
after add [text: "report"] => [task: t], pending work includes t;
then complete [task: t] => [] removes it from pending work;
then reopen [task: t] => [] restores the same t and text.
## queries
_pending [] => [task: Task; text: Text]
  returns exactly tasks minus done, one row per task with its text;
  zero rows when empty; order unspecified; no completion
```

| Acceptance from fresh state | Expected observation |
| --- | --- |
| add("report"), then _pending | Exactly the returned task and input text. |
| add to obtain t; complete(t), then reopen(t), querying after each | t disappears, then returns with unchanged text. |
| complete(t) twice, then reopen(t) twice | Repeats succeed without duplicate tasks or other changes. |
| complete(unknown) or reopen(unknown) | Missing with unchanged state. |
| _pending before add | Zero rows without an error. |

These are specified checks, not executed tests.
Deleting text during complete breaks reopening even if a complete-only test passes.
UI, external-entry, and durable-store behavior need additional contracts.
Todo needs one CONCEPT and no SYNCS.

## Partial reservation model

This fragment covers a selected slot's success or conflict.

```text
# concept Reserving [U, S]
coverage: partial
## purpose
Commit a resource slot to a user for future use.
## state
reservations: set Reservation
user: Reservation -> U
slot: Reservation -> S
status: Reservation -> Status
Reservation is local; Status = booked | canceled | granted.
Conflict is the singleton error for a slot with a booked reservation.
Initially reservations is empty.
Each reservation has one user, slot, and status.
Each S has at most one booked reservation; S has no assumed fields.
Illustration: after reserve [user: u1; slot: s1] => [reservation: r1] from empty state, one current reservation record is { reservation: r1, user: u1, slot: s1, status: booked }, identified by reservation, with other fields mapping to the same-named relations.
## actions
reserve [user: U; slot: S] => [reservation: Reservation]
  requires slot has no booked reservation
  ensures atomically creates and returns fresh r with input user/slot and booked status;
          adds r to reservations; existing facts are unchanged
reserve [user: U; slot: S] => [error: Conflict]
  requires slot has a booked reservation
  ensures returns Conflict; state is unchanged
cancel [reservation: Reservation] => []
  requires reservation is booked
  ensures changes only its status to canceled
grant [reservation: Reservation] => []
  requires reservation is booked; arrival conditions are open
  ensures changes only its status to granted
## operational principle
after reserve [user: u; slot: s] => [reservation: r],
then, if not canceled and arrival conditions hold, grant [reservation: r] => [] fulfills the commitment.
```

Availability[V] independently lets users find offered slots at a venue.
The required interface fragment declares local Slot identities, `venue: Slot -> V` with one venue per slot,
and `offered: set Slot` as a subset of existing slots.
Its `_find [venue: V] => [slot: Slot]` query returns every matching offered slot, one per row.
No match returns zero rows without a completion.
Availability never reads Reserving.

The application's entry contract is:

```text
Requesting/reserve: [user: UserId; slot: Availability.Slot] => [request: RequestId]
Requesting/respond: [request: RequestId; reservation: Reserving.Reservation] => []
Requesting/respond: [request: RequestId; error: Conflict] => []
```

Each request starts one runtime flow and carries its RequestId to the response.

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

The response rules require both completions in one flow with matching user/slot.
They discriminate success from error by output fields.
This fragment assumes one reservation attempt per request flow.
Repeated attempts would also need occurrence correlation.
No rule waits for _find; queries are reads, not completions.
Multiple candidates do not authorize reserving all of them.

A known-slot product may need only Reserving.
Discovery requirements, not type binding alone, justify retaining Availability.
Removing it requires rebinding S to an independently supplied SlotId and updating entries/rules.
A dangling Availability.Slot reference is not a usable subset.

Arrival inputs/timing, failed cancel/grant conditions, authentication, venue checks, concurrent withdrawal,
display, cancellation entries, and fault handling remain open.
Offered state can change before reserve; it does not enforce a write-time invariant.
Purpose fulfillment remains incomplete until arrival and grant are defined and checked.
