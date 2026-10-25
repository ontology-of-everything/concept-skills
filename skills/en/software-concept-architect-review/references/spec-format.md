# Concept and Synchronization Specification Contract

Read this before creating, transcribing, implementing, or checking CONCEPT and SYNCS files. The
format adapts WYSIWID v1 sections 4–6; it is repository notation, not executable engine syntax.

## Synchronization Principle

**Synchronization may restrict behavior, never extend the contract** (after *The Essence of
Software*): composition may exclude some original behaviors, but each concept's actual behavior
must still satisfy its own specification.

For each concept, retain only its actions, state changes, and outputs from a composed execution;
the resulting sequence must be allowed by its specification. Check sequences, not just action
names. Keep synchronization restrictions in SYNCS; preconditions, invariants, effects, and result
cases remain governed by the concept contract. Revise and confirm that contract before requiring
behavior beyond it.

Restriction alone is not a violation. Separately check whether the remaining scenarios fulfill
the purpose: a legal composition can still frustrate the need.

## CONCEPT: Independent Behavioral Interface

Write purpose → state → actions → operational principle. Put the concept name and optional type
parameters in the title. Repository-specific Markdown headings, requires/ensures, notes, and queries
extend the paper format. Mark every unconfirmed value as open.

```markdown
# concept Name [T]

## purpose

<one evaluable need>

## state

items: set Item owner: Item -> T <identity types, cardinality, initial state, invariants>

## actions

act [item: Item; owner: T] => [item: Item] requires <success condition> ensures <state change,
output, unchanged state> act [item: Item; owner: T] => [error: E] requires
<error condition and meaning of E> ensures <error value and state consequence>

## operational principle

after <condition and declared action input => output> then
<later action or observation and how the result fulfills purpose>
```

- External identity is a field-free type parameter. Define local types. Instantiate concrete types
  only in SYNCS.
- Purpose states one need, not a feature list.
- State states cardinality, initial state, and invariants. `A -> B` states only that the types are
  related, not that the relation is total or unique.
- Actions name inputs and outputs. Write `[]` for no parameters and `=> []` for no result. Each case
  states the condition, effect, and output.
- The OP uses real action names to show how the purpose is fulfilled. It does not enumerate behavior.

One action may have multiple cases. Field names are part of the matching contract. Distinguish
success and refusal conditions; if overlapping cases have different effects, define selection or
mark it open. Neither failure-state preservation nor success-state mutation is implicit.

Specifications may omit details irrelevant to the design, but must state every signature, branch,
and state meaning that affects synchronization. Resolve behavior-changing ambiguity before
implementation without inventing errors, authorization, or features to fill a template.

## Abstract State and Optional Queries

A concept owns and maintains its state. Applications may query exposed abstract state, including
joins, without exposing physical tables, private storage, or another concept's implementation.
Concepts still never call or read one another.

By default, `where` reads declared relations. A project with query interfaces may add `## queries`
containing named `_` query parameters, results, zero/one/many-row semantics, and the abstract-state
mapping. Queries are read-only and emit no completion. They are a local mapping, not a fifth core
section.

```text
_owners [item: Item] => [owner: T]
  returns matching owner bindings; no match returns zero rows
```

A synchronization may write `Name/_owners: [item: ?item] => [owner: ?owner]` in `where`, never in
`when` or `then`. Preserve uncertainty about initial state, cardinality, or query support; do not
turn an empty set into an undeclared error.

## SYNCS: Application Causal Rules

`app`, `include`, type instantiation, and `// flow:` are repository organization. `sync`, `when`,
`where`, and `then` use the paper's record patterns. Every include resolves to a concept
specification or an explicit external-entry contract. Define aliases and concrete types. Web is only
an example entry. An existing Requesting concept may keep its name if the signature is stated.
Timers and messages declare their own root events.

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

- `sync` is a stable, application-unique rule name representing one explainable decision.
- `when` is required and matches completed actions as
  `Concept/action: [input pattern] => [output pattern]`. Multiple patterns are conjunctive within
  one runtime flow.
- Patterns constrain only written fields; omitted fields are wildcards. `[]` is an empty pattern,
  not proof of success. Match a proven success discriminator when an action can return errors.
- `where` optionally reads abstract state, filters, computes, or binds. It consumes `when` bindings
  and returns zero, one, or many binding sets.
- `then` is required and emits calls for every binding set. Calls contain named inputs and no `=>`
  output. Supply the real signature; wildcard matching never permits missing call parameters.
- `?name` has one value throughout a rule. `then` uses only constants or variables bound by
  `when`/`where`. Calls in one `then` have no implicit order; future outputs are matched by another
  synchronization.

## Failure, Correlation, and Replay

- Match declared errors with `=> [error: ?error]` and ordinary negative results with fields such as
  `=> [valid: false]`. Authorization or validation must complete before a write; a later refusal
  cannot undo a completed write.
- Zero `where` rows produce no calls; multiple rows expand calls. Define zero-row response behavior
  for request entry points, and never choose the first candidate or all candidates without a
  contract.
- Flow separates root events. Correlate repeated same-kind actions with business IDs, not only a
  flow token. `request` locates a response; `// flow:` groups rules but is not a runtime token.
- Preserve partial completion. Define response, retry, compensation, or intentional ignore. A state
  snapshot cannot replace an atomic invariant check inside the action.
- Record action identity, flow, triggering rule, causal source, and emitted calls. Persist triggered
  matches to prevent replayed emission. Verify engine-specific deduplication; this does not
  guarantee exactly-once external effects.

## Compatibility and Delivery Check

Read legacy `principle`, old section order, `act (arg: T) : (result: R)`,
`Concept.act (...) : (...)`, and action-local `_` queries without treating syntax alone as drift.
New files use this contract; local edits preserve the current dialect unless migration is authorized
with all consumers and diagrams.

Before translating a legacy rule, recover inputs, outputs, success/error discrimination, and
correlation. Never convert an omitted legacy output into `=> []` if that would also match errors.

Check in order: type instantiation → state/query → action inputs and results → `when` case → `where`
cardinality → `then` parameters → entry response/correlation. Keep OP and application-scenario
provenance separate, cross-concept policy only in SYNCS, and purpose, dependencies, exclusions, and
open decisions in the overall PRD.
