# Engineering architecture

This layout is a repository choice, not Jackson's prescribed implementation.
New projects SHOULD use a modular monolith.
Each concept builds and tests independently; composition and protocol adapters build with server and have separate behavior tests.
Assemble in one process.
Existing confirmed conventions take precedence.

## Ownership and shape

```text
apps/server/
  src/
    bootstrap/                    # construction and final assembly
    adapters/http/                # protocol conversion
    compositions/booking/
      BookingFacade               # optional entry
      make_reservation/
        SYNCS.md
        CreateReservationSync
        ConfirmReservationSync
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
| Concept | MUST own its business state. MUST NOT import another concept, invoke its actions/queries, or read its state. Use generic or opaque external identities. |
| Domain | MUST enforce invariants without dependencies on application, adapters, HTTP, or ORM. |
| Application | Uses domain behavior; declares needed ports. A domain-specific port may belong in domain. |
| Adapter | Implements an inner port. Avoid duplicate repositories/readers for the same responsibility. |
| Composition | Uses public concept actions/queries. MAY own execution records; MUST NOT duplicate concept business facts. |
| Protocol adapter | Converts protocol input/output through composition entries; MUST NOT import concept implementations. |
| Bootstrap | Production construction and assembly entry. Scoped test fixtures/test assembly MAY also construct concepts and fake ports. |
| Technical library | MUST NOT depend on concepts/compositions or hide business state/coordination. |

Business code MUST NOT resolve dependencies from a container.
Separate business exports from construction entries and restrict production construction access to bootstrap.
Keep value types with their model until shared meaning, constraints, ownership, and change responsibility are established.
Shared database facilities and migrations MUST preserve state ownership.

## Composition groups and identities

Group rules by business responsibility; a group may span contexts.
Colocate one SYNCS.md with each group and index all groups without duplicating definitions.
Group count need not match concepts, endpoints, or runtime flows.
Declare application instance identities, type bindings, and shared entry contracts once; groups reference them.
Repeated includes MUST resolve to the same declared instances, and bootstrap MUST preserve that mapping.

New implementations SHOULD use `<BusinessEffect>Sync`, such as `CreateReservationSync`.
Add a trigger qualifier only when effects otherwise share a name.
Preserve confirmed names and map native names explicitly.
Rule identity MUST be stable and application-unique across specifications, tests, and runtime records.
A file move MUST NOT rename persisted rule identity.
Default to one rule per file; small related rules MAY share a file while retaining separate identities.

Rules coordinate through concept actions and MUST NOT call one another directly.
An optional `<BusinessScope>Facade` exposes a stable entry; coordination stays in named rules.
For long waits, timeouts, and compensation, identify the required process state.
Reconsider concept boundaries if that state gains an independent business purpose and lifecycle.

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
