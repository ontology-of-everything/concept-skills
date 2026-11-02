# CONCEPT and SYNCS format

These are local Markdown conventions adapted from the [sources](sources.md).
They are not engine syntax.

## CONCEPT

New files MUST use this order. Each core section MUST contain a declaration.
`coverage: complete|partial` is local metadata declaring coverage, not engine syntax.

```markdown
# concept Name [T]
coverage: partial

## purpose
<one evaluable need>

## state
items: set Item
owner: Item -> T
<local types, cardinality, initial state, invariants>

## actions
act [item: Item; owner: T] => [item: Item]
  requires <success condition>
  ensures <effect, output, unchanged state>
act [item: Item; owner: T] => [error: E]
  requires <refusal condition>
  ensures <error meaning and state consequence>

## operational principle
after <declared actions and results>
then <later action or observation fulfilling purpose>
```

`requires` enables a case.
`ensures` relates before/after state and outputs.

- `A -> B` alone implies neither totality nor uniqueness.
- Actions MUST name inputs/outputs and define each case's conditions, effects, and unchanged state.
  No input is `[]`; no result is `=> []`.
- A false case precondition does not itself produce a completion or error.
  Invalid requests need a declared refusal or entry policy.
- Different effects MUST have distinguishable cases or a selection rule.
  Success need not change state; failure need not preserve it.
  Read-only actions still complete.
- Transitions MUST atomically preserve invariants.
  Resolve behavior-changing ambiguity before dependent implementation.

Optional `## queries` maps public relations to read APIs:

```text
_owners [item: Item] => [owner: T]
  returns owner bindings; no match returns zero rows
```

Declare signatures, cardinality, and underlying relations.
Queries MUST be read-only and have no completion.
In SYNCS, `Name/_query: [inputs] => [outputs]` appears only in `where`.
Do not turn empty query results into undeclared errors.

When useful, include one `state` example satisfying its types, cardinalities, and invariants, with grain, identity, observation point, and relation mapping.
Optional table or interface mappings state their confirmation status and reference state constraints or action/query contracts respectively.
Analytical fact tables additionally define grain, time semantics, applicable measures, and historical sources.

## SYNCS

Includes MUST resolve to concept or external-entry contracts.
Declare aliases, concrete types, and root signatures for requests, timers, or messages.

```text
# app AppName
include Source [Id]
include Target [Id]

sync Transfer
when { Source/finish: [] => [item: ?item] }
where { Source: { ?item owner: ?owner } }
then { Target/accept: [item: ?item; owner: ?owner] }
```

| Part | Constraint |
| --- | --- |
| `sync` | Stable, application-unique name for one decision. |
| `when` | Required and nonempty. All completion patterns MUST match in one runtime flow. |
| Patterns | Omissions are wildcards; `[]` is not success. MUST distinguish cases affecting later effects. |
| `where` | Optional. Read, filter, compute, bind rows; omission retains input bindings. |
| `then` | Required and nonempty. MUST call per binding row with all required named inputs and no outputs. |
| `?name` | One value per rule. Calls use constants or bound values. |

Calls in one `then` have no implicit order.
Use later results for ordering.
`where` reads evaluation-time state.
Snapshots, locks, and reevaluation on later changes are not implied.
Required consistency MUST be explicit.

## Execution checks

- An invocation requests execution; a completion records its result.
  Occurrence identity connects them; equal arguments do not.
- A flow contains a root occurrence and its causal descendants.
  Repeated actions need occurrence/cause correlation as well as request/business identity.
  Specify all matches or a particular attempt.
  `// flow:` only labels documentation.
- Old completions from independent flows MUST NOT satisfy `when`.
  Use `where` for persistent facts and an entry/correlation protocol for delayed callbacks.
- Match errors separately from values such as `valid: false`.
  Required access checks MUST precede protected effects.
  Later refusal does not undo writes.
- Zero rows emit no calls; multiple rows expand calls.
  Specify required zero-match responses and candidate selection.
- Later failures MUST NOT erase existing completion records.
  Define responses, retries, compensation, or intentional ignore and their effects.
- Verify firing identity and atomic deduplication for occurrence tuples and rows.
  Reevaluation MUST preserve legitimate repetitions and prevent forbidden duplicates.
- In-memory records MAY suffice without restart recovery.
  Required recovery MUST persist occurrence, flow, rule/version, cause, bindings, and calls consistently.
  External effects need separate idempotency.

## Compatibility

Syntax alone is not drift.
Accept legacy `principle`, section order, `act (arg: T) : (result: R)`, `Concept.act (...) : (...)`, and action-local `_` queries.
Local edits SHOULD retain the dialect.
Migration MUST preserve signatures, result cases, correlation, and open decisions.
Do not turn omitted output into error-matching `=> []`.
Distinguish transactional synchronization from causal rules.
Update consumers and diagrams together.

## concept-lint

```sh
python3 scripts/concept_lint.py CONCEPT.md SYNCS.md --json
```

The read-only standard-library CLI checks declarations, coverage, unique/nonempty core sections, rule blocks, and rule-body delimiters.
In closed `when`/`then` blocks, it checks action input records, completion outputs in `when`, and absence of outputs in `then`.
Top-level input/output fields must be named, nonempty, and unique within their record.
Rule names must be unique across supplied files with the same `# app Name`; different apps may reuse names.
It preserves diagnostic line numbers while excluding comments, string contents, and fenced annotations from structural matching.
Unknown call notation is `not_checked`, including braced legacy dot-calls.
Nested record values and `where` expressions are opaque; includes, action signatures, types, and variable bindings are not resolved.
Concept independence, purpose, contract conformance, and runtime behavior require code review, architecture checks, or execution evidence.

| Exit | Status | Meaning |
| --- | --- | --- |
| 0 | `format_checked` | All inputs passed the listed structural checks. |
| 1 | `format_error` | At least one determined structural error. |
| 2 | `read_error` | Usage, file access, or encoding error. |
| 3 | `not_checked` | Legacy, unknown, incomplete notation, or missing coverage. |

Read errors take precedence over format errors; format errors take precedence over unchecked portions.
Incomplete comments, strings, or fences cannot turn hidden content into an inferred missing section.
Errors in already closed sections/blocks still count.
For a deliberately absent state or action set, write that declaration instead of leaving the section blank.
`format_checked` is not semantic verification.
