# Composition defect checklist

Start from application purpose and scenarios, then inspect concept selection, SYNCS, and the actual
mediator/engine and adapters. Check completion matching, bindings, correlation, and public-state
access against [the contract](spec-format.md).

| Category | Required evidence | Default | Route |
| --- | --- | --- | --- |
| Behavior violation | composed action/state/output sequence violates its concept contract | High | implementation; design if contract is absent |
| Implicit composition | one concept directly calls another, including public interfaces | High | implementation |
| Error/response gap | reachable result has no strategy, or a request hangs/crosses requests | High | design/implementation |
| Binding error | `then` uses an unbound/future output, or query cardinality is mishandled | High | design/implementation |
| Conjunction/correlation error | conjunctive triggers become alternatives or objects/requests are mismatched | High | design/implementation |
| Case-match error | empty output is treated as success or `valid=false` as error | High | design/implementation |
| Conflicting syncs | jointly enabled effects reproducibly violate state or require hidden order | High | design |
| Replay defect | redelivery causes disallowed duplicate effects | High | implementation |
| Dead sync | every supported entry is proven unable to produce its trigger | Low | PRD/design |
| Unbounded cascade | a reachable loop emits indefinitely without termination/control | High | design/implementation |
| Under/over-sync | a scenario shows missing coordination or lost user control | Medium | design |
| Misplaced invariant | composition query checks an invariant that an action must enforce atomically | High | implementation |
| Sync-owned domain state | orchestration acquires an independent purpose and lifecycle | Medium | design |
| Bypassing entry | interface skips confirmed authentication or coordination | High | implementation |
| Excluded action used | an explicitly excluded application action remains reachable | High | implementation/design |
| Diagram mismatch | derived graph loses conjunction, confuses query/trigger, or links incorrectly | Medium | PRD |
| Harmful synergy | composition distorts a concept purpose in an evidenced user scenario | Medium | design |

Use [severity calibration](drift-checklist.md#severity-calibration). A type-level cycle, absent depth cap,
long flow, dispersed rules, background work without HTTP response, or durable runtime log is not
itself a defect. Inspect the actual behavior. An occurrence graph may be acyclic despite repeated
rule firing; a directed acyclic graph does not prove termination.

Results may respond, retry, compensate, or be intentionally ignored under their contract; each
output need not have its own error rule. Declare a rule dead only after inspecting every supported
entry. Mark unscanned paths unverified. Valid query access alone proves neither system properties nor progress.

Merge repeated independence/drift/composition symptoms by root cause. Keep current source locations,
behavioral evidence, user consequences, and one current repair step.
