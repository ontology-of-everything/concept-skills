# Engineering architecture

These are this skill's engineering conventions, not Jackson's prescribed implementation. Default new projects to a modular monolith assembled in one process.
Use language-native source roots and confirmed build and persistence technology; fix directory roles, responsibilities, and dependencies as specified here.
Only explicitly confirmed exceptions may override this layout; record their scope. Existing code is not an exception, and migration stays within authorized scope.

## Directories and naming

```text
<application source root>/
  entry/<business module>/           # protocol entries and external adapters
  compositions/<business group>/
    <BusinessScope>Facade            # public business operations
    <BusinessAction>Synchronization  # internal synchronization implementation
  concepts/<concept>/
    api/                             # public commands, queries, business values
    application/                     # action/query implementations and inner ports
    domain/                          # state, invariants, behavior, repository contracts
    adapters/                        # port implementations, persistence, inner assembly
  bootstrap/                         # final assembly, controlled startup entries
```

- Fix layer names to `entry`, `compositions`, `concepts`, and `bootstrap`; use the concept layers shown above. Separate builds may relocate source roots while preserving roles and boundaries.
- Use lowercase singular business module, composition group, and concept directory names. Keep the same word stem for the same business scope. Match composition groups to specification directories; entries, groups, and concepts need not correspond one-to-one.
- Java packages are lowercase with joined compound words, such as `operatorsession`; other languages encode the same business name using native naming conventions. Types and methods follow language conventions.
- Name facades `<BusinessScope>Facade` and synchronizations `<BusinessAction>Synchronization`; do not add `UseCase` or `Mediator` intermediate layers. Functional implementations preserve equivalent roles and visibility.
- Use singular business subjects in type names; use plurals for list operations and collection variables, such as `ReadBookingsSynchronization` and `bookings`. REST paths follow interface contracts.
- Give each concept its own source package or module. Within authorized scope, prefer removal, consolidation, or reuse; add only structure needed to fulfill the contract. Do not nest domain layers inside composition groups or create a build unit per rule.

For Java/Spring explicit assembly, use `<Concept>Configuration` in `concepts/<concept>/adapters/`, `<BusinessScope>Configuration` in `compositions/<group>/`, and `<Application>Configuration` in `bootstrap/`. Create these only when needed; construct and wire components without business operations or decisions. Bind configuration values in `<Capability>Properties` at the consumer boundary, separate from assembly. Other languages preserve these responsibilities using native assembly conventions.

## Layer responsibilities and dependencies

Business calls follow `Entry → Facade → Synchronization → Concept API`. Use APIs for business access and dedicated entries for assembly. Adapters implement inner ports, keeping source dependencies inward.

| Owner | Responsibility and boundary |
| --- | --- |
| Entry | Group controllers, filters, and jobs by business module. Handle protocol parsing, format validation, trusted context, and response conversion; outbound adapters implement composition ports. Route business operations only through Facade; keep shared protocol mechanisms here. |
| Facade | Expose application operations, holding only synchronization collaborators. Each operation forwards exactly once, without business branches, transactions, or failure handling. Use ordinary application types; concept API values may be reused. |
| Synchronization | Connect root actions and explicitly organize cross-concept conditions, authorization rechecks, order, transactions, and failure policies from SYNCS. Access only concept APIs and required ports; keep implementations private to composition. |
| Composition helper | Reuse computations or execution mechanisms; keep business steps and branches in synchronizations. Never invoke synchronizations or Facade. |
| api | Expose business contracts and values, separating commands and queries by caller capability; depend on no concept internal layers. |
| application | Implement the API with domain behavior and inner ports for local actions and queries; do not depend on adapters. |
| domain | Own transitions, invariants, and aggregate repository contracts; depend on no other layers. A concept is not an aggregate. |
| adapters | Implement concept ports; contain SQL, mappers, database records, and inner assembly. Repositories persist aggregates; query ports read projections. Define one port per responsibility. |
| Bootstrap | Construct and assemble components, delegating to factories or configuration. Business calls still use Facade; test assembly may construct concepts and fake ports. |
| Technical library | Provide technical capabilities without dependencies on concepts or composition, hidden business state, or coordination. |

Three boundaries apply throughout:

- **Independent concepts.** Each owns its state and invariants. Forbid inter-concept dependencies, action/query calls, and state reads, and dependencies on Entry, composition, or Bootstrap. Use type parameters or opaque external identities without importing another concept's internals.
- **Coordination in composition.** Depend on neither Entry, Bootstrap, nor concept internals, including through helpers. Synchronizations never call one another or Facade. Composition defines ports implemented by Entry adapters; it may retain execution records, not copies of concept business facts.
- **Separate business and technology.** Keep protocol types out of business contracts and api/application/domain independent of frameworks and persistence. Inject dependencies through assembly; business code never queries a container. Give shared values, database facilities, and migrations explicit owners.

## Synchronization boundaries

Composition is the layer; Synchronization implements rules. Group by business responsibility, possibly across contexts. Default to one implementation per rule; explicitly map splits for independent trigger, transaction, or recovery boundaries. Shared implementations retain each rule's identity. Class length and method count do not define boundaries; extract helpers for implementation complexity alone.

Connect rules through completions, applying [execution and recovery](execution.md) for matching, causality, atomic claims, and applicable transactions and recovery. Reconsider concept boundaries when process state acquires an independent business purpose and lifecycle.

## Specification ownership

| Content | Authoritative location |
| --- | --- |
| Concept | `CONCEPT.md` beside the concept module; before modules exist, `docs/prd/concepts/<name>/CONCEPT.md`. |
| Synchronizations | `SYNCS.md` beside rules in `compositions/<group>/`; before modules exist, `docs/prd/compositions/<group>/SYNCS.md`. |
| Acceptance | Overall PRD or an existing acceptance file, linked to contracts or scenarios. |

Index all specifications in the overall PRD. Preserve a single authoritative source at other confirmed locations; do not move it without authorization.
Declare instance identities, type bindings, and shared entry contracts once. Repeated includes resolve to the same declared instances, and assembly preserves that mapping.
Rule identities are unique within the application and consistent across specifications, tests, and runtime records. Moves and renames must not change persisted identities.
Maintain the rule-to-implementation and entry-method mapping in documentation. Code names express business meaning; comments explain constraints and reasons. Do not name code after specification IDs.
Files and `// flow:` groups do not create runtime flows or require separate builds.

## Review and verification

Architecture checks must cover all relevant source/build units and supported configurations and run in normal checks or CI:

- Verify directories, singular/plural naming, module discovery, and rule mappings. Empty matches, omitted modules, and unresolved dependencies are gaps, not passes.
- Check actual dependencies, visibility, and cycles: concept independence, API-only access, inward dependencies, port ownership, assembly access, and technical library boundaries.
- Check that each Facade operation forwards exactly once, without branches, exception decisions, or other calls; prevent forbidden calls from synchronizations and helpers.
- Check business contracts and concept api/application/domain for leaked protocol, framework, or persistence types; verify active adapters.
- Fail each violation with its rule, source, target, and location. Use isolated counterexamples to verify rejection.

For Rust, inspect the build graph and within-crate boundaries; for Java, subpackage visibility and discovered modules; for TypeScript, aliases and type-only imports.
Test concepts, composition, protocols, and assembly separately. Verify conditions, transactions, failures, and concurrency through behavior tests; static checks are not behavioral evidence.
For requested product subsets, also check purpose, entries, rules, resources, build flags, and release ownership.
Report limits such as reflection, dynamic lookup, and cross-owner SQL; follow [execution and recovery](execution.md) for migration.
