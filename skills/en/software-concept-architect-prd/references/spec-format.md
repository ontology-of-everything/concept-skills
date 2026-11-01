# Concept and synchronization contract

Use this contract to write or check CONCEPT and SYNCS. It adapts
[WYSIWID v1 sections 4 to 6](https://arxiv.org/html/2508.14511v1#S4).
Markdown headings, requires/ensures, queries, and app declarations are local conventions, not engine syntax.

## Preserve concept behavior

Composition may restrict behavior, but each concept's action, state, and output sequence must remain
within its contract. Keep application restrictions in SYNCS; the concept owns preconditions,
invariants, effects, and result cases. Confirm a revised contract before requiring new behavior.
Also check purpose fulfillment, since a legal restriction can prevent a useful result.

## CONCEPT

Use this order for new specifications. Leave unconfirmed behavior open.

```markdown
# concept Name [T]

## purpose
<one evaluable need>

## state
items: set Item
owner: Item -> T
<define local identity Item, cardinality, initial state, and invariants>

## actions
act [item: Item; owner: T] => [item: Item]
  requires <success condition>
  ensures <state change, output, and unchanged information>
act [item: Item; owner: T] => [error: E]
  requires <error condition and meaning of E>
  ensures <error value and state consequence>

## operational principle
after <conditions and declared action input => output>
then <later action or observation and the useful result>
```

| Element | Check |
| --- | --- |
| Types | External identities are field-free parameters. Define local types; instantiate concrete types in SYNCS. |
| Purpose | State one evaluable need. |
| State | Declare cardinality, initial state, and invariants. `A -> B` alone means neither totality nor uniqueness. |
| Actions | Name inputs/outputs. Use `[]` for no inputs and `=> []` for no result. State each case's condition, effect, and output. |
| OP | Use declared actions to explain a useful result, not every possible behavior. |

Field names affect matching. Distinguish success and refusal; define selection for overlapping cases
with different effects, or mark it open. Failure need not preserve state, and success need not change it.
Read-only actions still produce completions. Preserve details affecting coordination; resolve
behavior-changing ambiguity before implementation without inventing errors, permissions, or functions.

## State and queries

Applications may read public abstract state, including joins, through its declared interface.
This opens neither private tables nor implementations. Concepts do not call or read one another.

`where` reads declared relations. Optional `## queries` may map those relations to an API:

```text
_owners [item: Item] => [owner: T]
  returns matching owner bindings; no match returns zero rows
```

Declare inputs, results, cardinality, and the underlying relation. Queries are read-only and produce
no completion; they are not a fifth core section. Use
`Name/_owners: [item: ?item] => [owner: ?owner]` only in `where`. Do not add a getter per field or
turn empty results into undeclared errors. Mark unknown state/cardinality/query facts open.

## SYNCS

Every include resolves to a concept specification or an explicit external-entry contract.
Define aliases, types, and entry signatures. Requesting/Web is one option; timers and messages need
root actions too.

```text
# app AppName
include Source [Id]
include Target [Id]
include Web

// flow: transfer
sync Transfer
when {
  Web/request: [method: "transfer"] => [request: ?request]
  Source/finish: [] => [item: ?item]
}
where {
  Source: { ?item owner: ?owner }
}
then {
  Target/accept: [item: ?item; owner: ?owner]
}
```

This is a notation example. Check Source.owner, target inputs, and response obligations against
actual contracts.

| Part | Meaning |
| --- | --- |
| `sync` | A stable, application-unique name for one explainable decision. |
| `when` | Required. Match completed actions as `Concept/action: [inputs] => [outputs]`. All patterns share one runtime flow. |
| Patterns | Omitted fields are wildcards. `[]` does not mean success; match a proven discriminator when errors are possible. |
| `where` | Optional. Read state, filter, compute, or bind zero or more rows. If absent, retain the input bindings. |
| `then` | Required. Emit calls for every binding row, with all named inputs and no output pattern. Wildcard matching does not permit omitted call arguments. |
| Variables | `?name` has one value per rule. Calls use constants or bound values. Calls in one `then` have no implicit order; another rule matches later outputs. |

## Results and correlation

- Match declared errors separately from negative values such as `valid: false`. Obtain authorization
  before writing; later refusal cannot undo a completed write.
- Zero query rows emit no calls; multiple rows expand calls. Define required zero-match responses.
  Choosing the first candidate or acting on all candidates needs a contract.
- A flow identifies one root event and its descendants. Repeated actions also need object identity.
  Request identity locates the response; `// flow:` only groups documentation.
- Preserve completed actions. Define response, retry, compensation, or intentional ignore and its
  state consequences. Actions check invariants atomically; a prior query cannot replace that check.
- When recovery is needed, retain action identity, flow, rule, cause, bindings, and emitted calls.
  Verify engine deduplication so replayed matches do not emit again. External effects need separate
  idempotency guarantees.

## Compatibility and checks

Accept legacy `principle`, section order, `act (arg: T) : (result: R)`,
`Concept.act (...) : (...)`, and action-local `_` queries. Syntax alone is not drift.
New files use this contract; local edits retain the existing dialect unless migration is authorized.

Before migrating, recover inputs, outputs, success/error discrimination, and correlation.
Do not replace an omitted output with `=> []` if that also matches errors. Identify older transactional
sync and wyx boundary sections separately. Preserve behavior and open decisions; update all consumers and diagrams.

Check types, state/queries, action results, matched cases, query cardinality, call arguments, and
correlated responses. Trace OPs and application scenarios separately. Cross-concept policy belongs
in SYNCS; purpose, product dependencies, exclusions, and open decisions belong in the overall PRD.
Implementation also checks concurrency, recovery, and observable results.
