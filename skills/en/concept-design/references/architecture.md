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
    adapters/                  # port implementations, persistence, inner assembly
  bootstrap/                         # final assembly, controlled startup entries
```

- Fix layer names to `entry`, `compositions`, `concepts`, and `bootstrap`; use the concept layers shown above. Separate builds may relocate source roots while preserving roles and boundaries.
- Use lowercase singular business module, composition group, and concept directory names. Keep the same word stem for the same business scope. Match composition groups to specification directories; entries, groups, and concepts need not correspond one-to-one.
- Java packages are lowercase with joined compound words, such as `operatorsession`; other languages encode the same business name using native naming conventions. Types and methods follow language conventions.
- Name facades `<BusinessScope>Facade` and synchronizations `<BusinessAction>Synchronization`; do not add `UseCase` or `Mediator` intermediate layers. Functional implementations preserve equivalent roles and visibility.
- Use singular business subjects in type names; use plurals for list operations and collection variables, such as `ReadBookingsSynchronization` and `bookings`. REST paths follow interface contracts.
- Give each concept its own source package or module. Create layers only for actual responsibilities and remove scoped empty placeholders. Do not nest domain layers inside composition groups or create a build unit per rule.

## Layer responsibilities and dependencies

Fix the business call chain to `Entry → Facade → Synchronization → Concept API`.
Arrows denote business calls; adapters implement inner ports to keep source dependencies inward. Bootstrap may access assembly entries, not invoke synchronization implementations.

| Owner | Hard constraint |
| --- | --- |
| Entry | Group controllers, filters, jobs, and similar entries by business module. Inbound entries handle protocol parsing, format validation, trusted context extraction, and response conversion; outbound adapters implement composition ports. Route business operations through Facade; do not invoke synchronizations or concept actions/queries. Keep shared protocol mechanisms in this layer. |
| Facade | Expose application operations; each operation method forwards exactly once to its synchronization. Hold only synchronization collaborators; do not decide business conditions, open transactions, handle failures, or invoke concepts or external adapters. |
| Synchronization | Map entry inputs to the declared root action; own cross-concept conditions, authorization rechecks, action order, transactions, and failure policies according to SYNCS. Access business capabilities only through concept APIs and required ports. Keep implementations inaccessible outside composition. |
| Composition helper | Reuse named computations or execution mechanisms; keep business steps, order, and branches explicit in synchronizations. Do not invoke synchronizations or facades. |
| Concept | Own its state and invariants. Forbid source dependencies, action/query calls, and state reads between concepts. Use generic or opaque external identities without another concept's internal structure. |
| api | Expose only business contracts and values, separating commands and queries by caller capability. Do not depend on concept internal layers or expose protocol, framework, or persistence types. |
| application | Implement the API using domain behavior and inner ports; organize concept-local actions and queries. Do not depend on adapters. |
| domain | Own state transitions, invariants, and aggregate repository contracts. Do not depend on api, application, adapters, or framework/persistence types. A concept is not an aggregate. |
| adapters | Implement inner ports; contain SQL, mappers, database records, and internal assembly. Persist aggregates through repositories and read projections through query ports. Define only one port per responsibility. |
| Bootstrap | Own final construction and assembly, delegating to module factories or configuration as needed. Route business calls through Facade. Test assembly may construct concepts and fake ports. |
| Technical library | Do not depend on concepts or composition, or hide business state or coordination. |

Concepts must not depend on Entry, composition, or Bootstrap. Composition must not depend on Entry, Bootstrap, or concept internals, including through helpers. Synchronizations must not call one another or call back into Facade.
Composition defines its ports, implemented by Entry adapters; concept ports are implemented within that concept’s adapters.
Facade uses ordinary application types and may reuse concept API values; protocol types must not cross business contracts.
Keep api, application, and domain independent of framework and persistence types. Business code must not resolve dependencies from a container. Separate business exports from assembly entries.
Composition may store execution records but must not duplicate concept business facts. Shared values, database facilities, and migrations must preserve explicit ownership.

## Synchronization boundaries

Composition is the layer; Synchronization implements its rules. Group by business responsibility, potentially across contexts.
Default to one implementation per named rule; map splits explicitly when triggers, transaction boundaries, or recovery boundaries are independent. Related operations may share an implementation, but each rule retains its own identity.
Class length and method count do not determine boundaries; extract helpers when only implementation complexity grows.

Connect rules through action completions, never direct calls. Preserve same-flow matching, prerequisites, causal provenance, and atomic firing claims under [execution and recovery](execution.md). Apply declared transaction and recovery requirements; ordinary calls do not waive execution guarantees.
Reconsider concept boundaries when process state gains an independent business purpose and lifecycle.

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
