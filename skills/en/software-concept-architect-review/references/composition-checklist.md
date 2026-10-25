# Composition Defect Checklist

Start from the application purpose and end-to-end scenarios in requirements or the overall PRD, then
inspect concept selection, SYNCS, and the mediator/engine and interface adapters. Under WYSIWID
causal semantics, `when` matches completions, `where` produces bindings, and `then` emits calls.
Multiple `when` records share a flow and errors are explicit. `where` may read public abstract state
or declared queries while physical storage stays private; see `spec-format.md`.

| Category                      | Required evidence                                                                | Default | Route                                        |
| ----------------------------- | -------------------------------------------------------------------------------- | ------- | -------------------------------------------- |
| Behavior violation            | composed action/state/output sequence violates its concept contract              | High    | implementation; design if contract is absent |
| Implicit composition          | one concept directly calls another, including public interfaces                  | High    | implementation                               |
| Error/response gap            | reachable result has no strategy, or a request hangs/crosses requests            | High    | design/implementation                        |
| Binding error                 | `then` uses an unbound/future output, or query cardinality is mishandled         | High    | design/implementation                        |
| Conjunction/correlation error | conjunctive triggers become alternatives or objects/requests are mismatched      | High    | design/implementation                        |
| Case-match error              | empty output is treated as success or `valid=false` as error                     | High    | design/implementation                        |
| Conflicting syncs             | jointly enabled effects reproducibly violate state or require hidden order       | High    | design                                       |
| Replay defect                 | redelivery causes disallowed duplicate effects                                   | High    | implementation                               |
| Dead sync                     | every supported entry is proven unable to produce its trigger                    | Low     | PRD/design                                   |
| Unbounded cascade             | a reachable loop emits indefinitely without termination/control                  | High    | design/implementation                        |
| Under/over-sync               | a scenario shows missing coordination or lost user control                       | Medium  | design                                       |
| Misplaced invariant           | composition query checks an invariant that an action must enforce atomically     | High    | implementation                               |
| Sync-owned domain state       | orchestration acquires an independent purpose and lifecycle                      | Medium  | design                                       |
| Bypassing entry               | interface skips confirmed authentication or coordination                         | High    | implementation                               |
| Excluded action used          | an explicitly excluded application action remains reachable                      | High    | implementation/design                        |
| Diagram mismatch              | derived graph loses conjunction, confuses query/trigger, or links incorrectly    | Medium  | PRD                                          |
| Harmful synergy               | composition distorts a concept purpose in an evidenced user scenario             | Medium  | design                                       |

Calibrate through `drift-checklist.md`. A type-level cycle, absent depth cap, long flow, dispersed
rules, missing HTTP response for background work, or persisted runtime log is not a defect by
itself. Inspect actual behavior and project conventions. An occurrence graph may be acyclic despite
a loop, and a DAG does not prove termination.

Errors may respond, retry, compensate, or be intentionally ignored; one error sync per output is not
mandatory. Call a rule dead only after reading every supported entry. Mark unscanned paths
unverified. Merge repeated independence/drift/composition symptoms into one root cause with
locations, behavioral evidence, user consequence, and one current repair step.
