# CONCEPT and SYNCS format

This file defines the skill's Markdown specification conventions.
These conventions are not engine syntax.
For worked models and acceptance checks, use the [scenario index](examples.md#scenario-index).

Use adjacent, single-line `//` comments only for non-obvious choices or sources.
Behavior requirements MUST be stated in contracts or rules.
Recheck comments when those declarations change.

## Execution constraints

Record a concept's own execution requirements in `CONCEPT.md` and cross-concept requirements in `SYNCS.md`.
New CONCEPT/SYNCS files SHOULD include this section by default.
Reference existing action contracts and the [execution checks](#execution-checks); record the model's assumptions and policies without copying those definitions.
Cover completion, concurrency/order, correlation and repetition, failure effects, and required timing, retries, and recovery as applicable.
Record confirmed policies; mark unresolved items `open` and irrelevant items `not applicable`.
Execution requirements MUST state permitted observable behavior, required outcomes, and their assumptions.
Each requirement MUST identify its action contract or rule and acceptance checks.
Execution evidence MUST link actual effects to action occurrences, causal origins, and the applicable specification.

## CONCEPT

The four required core sections MUST appear in this order: `purpose`, `state`, `actions`, `operational principle`.
Each MUST contain a declaration.
Place optional `queries` after the operational principle, then the default execution-constraints section.
`coverage: complete|partial` declares the specification's coverage. It is local metadata.

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

## Execution constraints
- Completion: <when the declared result and state effects become observable>
- Concurrency: <atomic invariant checks and permitted concurrent behavior>
- Failure/repetition: <refusal effects and repeated-call or retry policy>
- Timing/recovery: <required bounds and persistence, or open/not applicable>
```

`requires` enables a case.
`ensures` relates before/after state and outputs.

- `A -> B` alone implies neither totality nor uniqueness.
- Actions MUST name inputs and outputs.
  Each case MUST define its conditions, effects, and unchanged state.
  No input is `[]`; no result is `=> []`.
- A false case precondition does not itself produce a completion or error.
  Invalid requests need a declared refusal or entry policy.
- Different effects MUST have distinguishable cases or a selection rule.
  Success need not change state; failure need not preserve it.
  Read-only actions still complete.
- Transitions MUST atomically preserve invariants.
  Resolve behavior-changing ambiguity before dependent implementation.

Optional `## queries` maps public relations to read APIs:

```markdown
## queries
_owners [item: Item] => [owner: T]
  returns owner bindings; no match returns zero rows
```

Declare signatures, cardinality, and underlying relations.
Queries MUST be read-only and have no completion.
In SYNCS, `Name/_query: [inputs] => [outputs]` appears only in `where`.
Do not turn empty query results into undeclared errors.

When useful, include one `state` example satisfying its types, cardinalities, and invariants.
State its grain, identity, observation point, and relation mapping.
Optional table or interface mappings state their confirmation status and reference the relevant state constraints or action/query contracts.
Analytical fact tables also define grain, time semantics, applicable measures, and historical sources.

## SYNCS

Includes MUST resolve to concept or external-entry contracts.
Declare aliases, concrete types, and root signatures for requests, timers, or messages.

A `sync` MAY be immediately preceded by `### <business description>`.

```markdown
# app AppName
include Source [Id]
include Target [Id]

### Pass completion results
sync Transfer
when { Source/finish: [] => [item: ?item] }
where { Source: { ?item owner: ?owner } }
then { Target/accept: [item: ?item; owner: ?owner] }

## Execution constraints
- Flow/correlation: <root occurrence, causal descendants, and repeated-attempt identity>
- Reads/order: <read consistency and completion dependencies>
- Outcomes: <success, refusal, zero matches, partial effects, and firing deduplication>
- Timing/recovery: <required bounds, retries, replay, and external idempotency, or open/not applicable>
```

| Part | Constraint |
| --- | --- |
| `sync` | Stable, application-unique name for one decision. |
| `when` | Required and nonempty. All completion patterns MUST match in one runtime flow. |
| Patterns | Omissions are wildcards; `[]` is not success. MUST distinguish cases affecting later effects. |
| `where` | Optional. Read, filter, compute, bind rows; omission retains input bindings. |
| `then` | Required and nonempty. MUST call per binding row with all required named inputs and no outputs. |
| `?name` | One value per rule. Calls use constants or bound values. |

`sync` defines causal rules.
It implies neither blocking execution nor cross-action transactions or rollback.
Calls in one `then` have no implicit order.
Use later results for ordering.
`where` reads evaluation-time state.
Snapshots, locks, and reevaluation on later changes are not implied.
Required consistency MUST be explicit.

[Synchronization scenarios](examples.md#synchronization-scenarios).

## Execution checks

- An invocation requests execution; a completion records its result.
  Occurrence identity connects them; equal arguments do not.
  Asynchronous actions MUST define when they complete.
  Acceptance or enqueue completion does not complete subsequent work.
- A flow contains a root occurrence and its causal descendants.
  Calls emitted by `then` and their completions MUST retain the triggering flow.
  Repeated actions need occurrence/cause correlation as well as request/business identity.
  Specify all matches or a particular attempt.
  `// flow:` only labels documentation.
- Old completions from independent flows MUST NOT satisfy `when`.
  Use `where` for persistent facts and an entry/correlation protocol for delayed callbacks.
- Match errors separately from values such as `valid: false`.
  Runtime exceptions handled by rules MUST map to declared result cases.
  Required access checks MUST precede protected effects.
  Later refusal does not undo writes.
- Zero rows emit no calls; multiple rows expand calls.
  Specify required zero-match responses and candidate selection.
- Later failures MUST NOT erase existing completion records.
  Define responses, retries, compensation, or intentional ignore and their effects.
- Verify firing identity and atomic deduplication for occurrence tuples and rows.
  Reevaluation MUST preserve legitimate repetitions and prevent forbidden duplicates.
- In-memory records MAY suffice without restart recovery.
  Required recovery MUST preserve pending work and causal correlation; use the [recovery protocol](engineering/execution.md#atomicity-and-recovery).
  External effects need separate idempotency.

## Compatibility

Syntax alone is not drift.
Local edits SHOULD retain a confirmed existing dialect; legacy notation may return `not_checked` from concept-lint.
Migration MUST preserve signatures, result cases, correlation, and open decisions.
Do not turn omitted output into error-matching `=> []`.
Distinguish transactional synchronization from causal rules.
Update consumers and diagrams together.

## concept-lint

```sh
python3 <skill-directory>/scripts/concept_lint.py CONCEPT.md SYNCS.md --json
```

The CLI is read-only and uses only the standard library.
It checks declarations, coverage, unique and nonempty core sections, rule blocks, and their delimiters.
In closed `when`/`then` blocks, it checks action input records.
It checks completion outputs in `when` and absence of outputs in `then`.
Top-level input/output fields must be named, nonempty, and unique within their record.
The checker detects duplicate rule names across input files with the same `# app Name`.
Different apps may reuse rule names.
Structural checks ignore comments, string contents, and fenced annotations while preserving diagnostic line numbers.
Unknown call notation is `not_checked`, including braced legacy dot-calls.
It does not resolve nested record values, `where` expressions, includes, action signatures, types, or variable bindings.
It does not require the recommended execution-constraints section or verify its policies.
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
