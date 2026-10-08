# Engineering Architecture

Read when defining or checking project structure. Principles live in [SKILL.md](../SKILL.md);
read build configuration only for the target language.

## Build and runtime boundaries

```text
apps/server/                     # sole startup application; configuration and assembly
modules/
  concepts/<group>/<concept>/    # each leaf is a build unit
    CONCEPT.md
    src/                        # public API + domain/application/adapter
  syncs/                        # independent build unit; public application API
    SYNCS.md                    # named rules grouped by flow
    src/                        # rules; execution ports/adapters when needed
  gateway/                      # independent build unit; protocol/DTO/error mapping
  shared/                       # independent build unit; passive foundational types
```

Groups and flows aid navigation; they do not automatically become modules. Building a module also
builds its declared dependency closure. Modules assemble into one process; separate builds do not
imply separate startup or deployment. A single-module task delivers only its required scope.

| Module | Business dependencies | Public surface |
| --- | --- | --- |
| concept | shared as needed | actions, queries, result types, necessary completion events |
| syncs | concept APIs, shared | application actions/results; signatures use syncs/shared types |
| gateway | syncs APIs, shared | external protocol; route/configuration entry for server |
| shared | no business modules | passive identity/time types |
| server | public assembly entries | startup; multi-module wiring is not business coordination |

Distinguish business APIs from assembly APIs; syncs uses only concept business APIs. Concepts
encapsulate storage. Database infrastructure may be shared, while reads/writes go through the owning
concept. Identify state owners in migrations.

## Internal dependencies

- `domain`: models, invariants, pure rules; the inner layer needing storage declares its port.
- `application`: implements public actions/queries, uses domain logic and ports, owns use-case transaction boundaries.
- `adapter`: implements ports against storage/external facilities; technical details depend on inner contracts.
- Assembly entry: constructs implementations and returns public interfaces while hiding internals.

Syncs application code holds named rules; recovery may require execution ports and adapters. Business
state remains in concepts. Gateway is an inbound adapter; add no domain layer for directory symmetry.
Use crate modules, Java packages, or TypeScript directories for internal layers; do not split every
layer into a build unit by default.

## One request, including failure

Example confirmed contract: Reservation produces Held, Confirmed, or Cancelled; Payment produces
Paid or Declined. Declined payment must eventually release the reservation. This causal sketch
does not replace the specification's exact fields and cases.

```text
gateway: HTTP request → syncs.reserve (establish request/flow correlation)
syncs: request completion → Reservation.hold
syncs: hold[Held] → Payment.charge
syncs: charge[Paid] → Reservation.confirm
syncs: confirm[Confirmed] → success response
syncs: charge[Declined] → Reservation.cancel
syncs: cancel[Cancelled] → declined response
gateway: application result → HTTP response
```

Each edge is a named rule binding a prior completion. Carry flow and reservation identity through
matching. If cancellation temporarily fails, completed hold/charge actions remain: persist pending
execution, respond under the confirmed entry contract, and retry cancellation without charging again.
Exhausted retries must be observable; do not claim release prematurely. Compensation does not erase
history. Sequential implementations must preserve the same correlation, branches, and recovery.

## Decisions that prevent mistakes

| Correct | Counterexample and consequence |
| --- | --- |
| module manifest, API, and test entry | folders alone cannot prove independent builds |
| gateway → syncs → concept API | controller orchestration or concept calls scatter application policy |
| inner port implemented by adapter | domain imports HTTP/SQL implementations and binds rules to infrastructure |
| restricted public factory/configuration for server | exposing every internal package lets business code bypass boundaries |
| named rules match cases and correlation | sequential `?`/exception propagation leaves partial state unmanaged |
| build graph plus source/API checks | acyclicity alone misses compilable but forbidden concept dependencies |

Verify module builds, API/layer boundaries, concept OPs/invariants, rule branches, and end-to-end
failure recovery separately. Static boundary checks do not establish correct behavior.
