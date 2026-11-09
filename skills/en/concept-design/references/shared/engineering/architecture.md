# Engineering architecture

This layout is a repository choice, not Jackson's prescribed implementation.
New projects SHOULD use a modular monolith.
Each concept builds and tests independently; composition and protocol adapters build with server and have separate behavior tests.
Assemble in one process.
Existing confirmed conventions take precedence.

## Architecture requirements

1. **Make concepts self-contained.** Define each concept's state and actions around one purpose. Each concept owns its business state. See the [concept specification](../model/spec-format.md#concept).
2. **Keep concepts independent.** Forbid source dependencies, action or query calls, and state reads between concepts.
3. **Compose concepts through synchronizations.** Express each application decision in a named rule outside the concepts. Access concepts through public actions and queries. See the [synchronization specification](../model/spec-format.md#syncs).
4. **Connect external entries through synchronizations.** Map external requests to root actions. Synchronizations invoke concept actions and trigger responses to the original requests.
5. **Preserve causal scope.** Match completions only within the same flow. Subsequent invocations carry that flow and retain their causal provenance.
6. **Specify failures and prerequisites.** Declare relevant failure branches. Invoke dependent actions only after their prerequisites are met.
7. **Fire once per match.** Before dispatch, atomically claim the firing by rule identity, matched completion records, and binding row. See [rule execution](execution.md#rule-execution).

## Ownership and shape

```text
apps/server/
  src/
    bootstrap/                    # construction and final assembly
    adapters/http/                # protocol conversion
    compositions/booking/
      reserve/
        MakeReservationUseCase
        SYNCS.md
        ReserveMediator          # sync reserve
        SuccessReplyMediator     # sync accepted
        ConflictReplyMediator    # sync rejected
  tests/                          # architecture, composition, protocol
modules/<context>/concepts/<concept>/
  CONCEPT.md
  <build manifest>
  src/
    <business exports>
    <assembly entry>
    domain/                       # state and invariants
    application/                  # actions and queries
      ports/                      # contracts needed by inner code
    adapters/                     # port implementations
  tests/
libraries/<technical capability>/ # optional independent build/tests
deploy/                           # environment and deployment
```

Context directories separate models and language; a concept is not a DDD aggregate.
Use native source roots from [language mapping](languages.md).
Small concepts MAY remain flat.
Do not create empty layers, per-rule build modules, or another domain/application/adapters stack inside each composition group.

| Owner | Constraint |
| --- | --- |
| Concept | Use generic or opaque external identities. |
| Domain | MUST enforce invariants without dependencies on application, adapters, HTTP, or ORM. |
| Application | Uses domain behavior; declares needed ports. A domain-specific port may belong in domain. |
| Adapter | Implements an inner port. Avoid duplicate repositories/readers for the same responsibility. |
| Composition | MAY own execution records; MUST NOT duplicate concept business facts. |
| Protocol adapter | Converts protocol input/output through composition entries; MUST NOT import concept implementations. |
| Bootstrap | Production construction and assembly entry. Scoped test fixtures/test assembly MAY also construct concepts and fake ports. |
| Technical library | MUST NOT depend on concepts/compositions or hide business state/coordination. |

Business code MUST NOT resolve dependencies from a container.
Separate business exports from construction entries and restrict production construction access to bootstrap.
Keep value types with their model until shared meaning, constraints, ownership, and change responsibility are established.
Shared database facilities and migrations MUST preserve state ownership.

## Composition groups and identities

Meng and Jackson describe synchronization as a mediator. It matches action completions and invokes subsequent actions when the conditions hold. See [WYSIWID §8](https://arxiv.org/html/2508.14511v2#S8).

Group rules by business responsibility. Groups may span contexts, and their boundaries are independent of concepts, endpoints, and flows.
Keep one [SYNCS.md](../model/spec-format.md#syncs) beside each group. Index every group and define each rule once.
Declare application instance identities, type bindings, and shared entry contracts once. Groups reference those declarations.
Repeated includes MUST resolve to the same declared instances, and bootstrap MUST preserve that mapping.
A single operation MAY use an `<Operation>UseCase` as its entry. Multiple operations MAY share a `<BusinessScope>Facade`.

New implementations SHOULD use `<BusinessEffect>Mediator`, such as `ReserveMediator`. Include the trigger when it clarifies or distinguishes the rule.
Preserve confirmed names and map native code names explicitly.
Rule identity MUST be unique within the application and stable across specifications, tests, and runtime records. A file move MUST NOT change persisted rule identity.
Default to one rule per file. Small related rules MAY share a file while retaining separate identities.

### Splitting synchronizations

- Split into named synchronizations when triggers, business effects, or failure policies can change independently.
- When one effect needs several prerequisite results, match all of them from the same flow in one `when` clause.
- Extract helper functions within the rule when only the implementation grows complex. Preserve rule identity and firing boundaries. Group rules separately when they form a distinct business responsibility.

Connect rules through action completions. Rules MUST NOT call one another directly.
Identify the process state required for long waits, timeouts, and compensation. Reconsider concept boundaries if that state gains an independent business purpose and lifecycle.

## Review and verification

Use [execution and recovery](execution.md) for required migration.
For requested product subsets, check purpose, dependencies, entries, rules, resources, build flags, and release ownership.

Architecture checks MUST inspect actual dependencies in all relevant source/build units and supported configurations.
Cover concept independence, public business API access, inner dependencies, protocol entries, construction access, libraries, cycles, specification ownership, and unique rule identities.
Run changed boundary checks in normal checks or CI.
An empty match, omitted module, or unresolved dependency is a gap, not a pass.
Each violation reports rule, source, target, and location and fails the check.
Use isolated violations to verify that the intended check fails.
Report limits such as reflection, dynamic lookup, and cross-owner SQL; add targeted checks where needed.

## Engineering basis

[DDD](https://www.domainlanguage.com/ddd/reference/) informs model boundaries.
[Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html) and
[Ports and Adapters](https://alistair.cockburn.us/hexagonal-architecture) inform dependency direction.
