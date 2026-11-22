# Engineering architecture

Concept and synchronization semantics follow Meng and Jackson; the engineering names and layout below are conventions of this skill. Default to an in-process modular monolith with language-native source roots. Confirm and document the scope of exceptions to the responsibility and dependency boundaries below.

## Design and engineering terms

| Design term | Engineering expression | Responsibility |
| --- | --- | --- |
| Concept | Business module at `modules/<business name>` | Independently own state, actions, and invariants |
| Concept composition | Use case group at `usecases/<business group>` | Organize application-specific coordination across modules |
| Synchronization rule | Named use case, internal method, or event handler | Implement a `when/where/then` causal rule |

Specifications retain concepts, compositions, synchronization rules, and `CONCEPT.md/SYNCS.md`. Engineering renames preserve the model and behavior. `modules` denotes business modules, not every technical module discovered by a framework; separate build or deployment units are not required.

## Directories and naming

```text
<source root>/
  entry/<business group>/           # inbound HTTP, protocol, event, and scheduled adapters
  usecases/<business group>/
    SYNCS.md                        # when colocating specifications
    <Action>UseCase                 # public entry rule
    <Action>On<Event>               # follow-up event rule
  modules/<business name>/          # dedicated business source package or module per concept
    CONCEPT.md                      # when colocating specifications
    api/                            # in-process public commands, queries, and value types
    application/                    # action/query implementations and inner ports
    domain/                         # state, invariants, behavior, repository contracts
    adapters/                       # port implementations, persistence, concept wiring
  adapters/                        # application-level outbound adapters, as needed
  contracts/                       # application-level exchange contracts, as needed
  infrastructure/                  # technical mechanisms, as needed
  bootstrap/                       # final wiring and startup
```

- Use these engineering names in new projects. In existing projects, record design-to-implementation mappings before authorized renames. Use lowercase singular business directories; retain fixed collection or role names such as `modules/usecases/contracts`. Reuse business word stems between modules and their concepts, and between use case groups and their compositions; module and use case groups need not share names. Join Java package words, as in `operatorsession`. Use singular type subjects and plural list operations and collections, as in `ReadBookingsUseCase` and `bookings`.
- Keep use case groups free of nested domain layers. Rules may share a source module or build unit. Functional implementations preserve roles and visibility. Consumers own their `ports`; `support` is limited to internal collaborators of its use case group. Local `contracts` belong to the exchanging consumer. Retain or add other business or technical packages according to actual responsibilities and record their dependency boundaries.
- Wire Java/Spring components as needed in `<Business>Configuration` under module `adapters/`, `<BusinessScope>Configuration` in the use case group, and `<Application>Configuration` under `bootstrap/`; existing module-specific wiring entries may retain their locations. Name collection wiring by its engineering role, as in `ModulesConfiguration`. Bind values in `<Capability>Properties` at the consumer boundary. Use native equivalents in other languages.

## Layer responsibilities and dependencies

- **Inbound adapter → public `<Action>UseCase` → business module API.** Entry handles protocol parsing, format validation, trusted context, and response conversion. Fold forwarding-only Facades into the use case entry. Application-level outbound adapters implement use case ports and default to top-level `adapters/`. Retain existing outbound implementations in `entry` under confirmed boundaries and document their roles; scope responsibility moves separately.
- **Business modules implement independent concepts.** Each owns its state and invariants. Forbid dependencies, calls, and state reads between concepts, and dependencies on entry, composition, or bootstrap. Use type parameters or opaque IDs for external identities.
- **Business module internals.** Keep `api` and `domain` independent of other layers. `application` depends on `api`, `domain`, and inner ports. `adapters` implement ports. Repositories persist aggregates and query ports read projections. Define one port per responsibility.
- **Use cases implement compositions and synchronizations.** Access concepts through business module APIs and depend on required inner ports. Forbid dependencies on entry or bootstrap. Keep business branches, authorization rechecks, transactions, and failure policy in rules. Helpers reuse computations or execution mechanisms without calling rules. Composition may keep execution records. Concepts own business facts.
- **Technology boundaries.** Keep protocol, framework, and persistence types out of business contracts and `api/application/domain`. Wiring constructs and injects components. Business code avoids container lookups. Technical libraries neither depend on nor coordinate business code. Application-level `contracts` define exchange boundaries without owning business facts; `infrastructure` supplies technical mechanisms while business branches remain in use cases or modules.

## Synchronization boundaries

The inbound adapter establishes or passes the root action completion and its flow. Give each rule one named implementation. Each public use case implements one entry rule. Match completions in `when`, evaluate optional `where`, and invoke actions in `then`. Same-transaction follow-up rules may use internal methods. Use `<Action>On<Event>` for rules shared across entries, independently scheduled, or independently recovered. Follow-up rules fire on their own matching completions. Apply the contract and [execution and recovery](execution.md) for transactions, causality, atomic claims, and recovery.

## Specification ownership

Specifications may sit beside implementations as `CONCEPT.md` in a business module and `SYNCS.md` in a use case group; retain existing separate design directories. Before modules exist, use the corresponding `concepts/<concept>/` or `compositions/<business group>/` under `docs/prd/`. For separate layouts, explicitly maintain the following mappings; retain design-defined concept names, instances and type bindings, and rule identities:

```text
<design root>/concepts/<concept>/CONCEPT.md → <source root>/modules/<business name>/
<design root>/compositions/<business group>/SYNCS.md → <source root>/usecases/<business group>/
```

Index authoritative specifications in the overall PRD and link acceptance to contracts or scenarios. Maintain each specification body in one place without duplicating it between colocated and separate layouts. Obtain authorization before moving confirmed locations.

Declare instances, type bindings, and shared entry contracts once. Repeated includes resolve to the same instance. Map each `SYNCS.md` rule to its use case, internal method, or event handler. Use the same rule identity across specifications, tests, and runtime records. Preserve persisted identities and trigger, transaction, failure, and retry semantics during migration. `// flow:` only groups documentation.

## Review and verification

Run checks on actual sources, build units, and configurations in normal checks or CI. Verify layout, naming, module discovery, design-to-implementation mappings, and dependency graphs. Check visibility, cycles, type leaks, and adapter wiring. Checkers explicitly distinguish design and source paths; dependencies, calls, and state reads between business modules remain violations. Fail violations with their locations and report missed coverage or unresolved dependencies as gaps. Behavior-test triggers, transactions, failures, retries, and concurrency.

For engineering renames, also check source and test paths, imports/exports, build manifests, framework module identities and interfaces, architecture matchers, wiring and scanning, configured qualified type names, and documentation links. Inspect stored names in persistent events, serialized types, and recovery records alongside release status before defining migration or compatibility scope; use the confirmed initial-release contract for unreleased systems. Run affected architecture checks, compilation, and behavior regressions to verify unchanged trigger, transaction, and recovery semantics.
