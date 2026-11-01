# Engineering architecture

Use this page for module responsibilities. Read only the target language mapping for build configuration.

## Dependencies and state

```text
api → composition → concepts
server assembles all modules through public factories
```

The first line shows business calls. Concepts never call or import one another.
Server assembles public factories; coordination stays in composition.

| Module | Allowed business dependencies | Public interface |
| --- | --- | --- |
| concept | Shared as needed | Actions, queries, result types, necessary completions |
| composition | Concept interfaces, shared | Application requests/results using its own or shared types |
| api | Composition interfaces, shared | Protocol mapping and route/configuration factories |
| shared | None | Passive identity/time types |
| server | Public assembly entries | Startup and configuration |

Each concept owns its business state and storage access. Database infrastructure may be shared,
but reads/writes go through the owner, identified in migrations. Composition may retain execution
records, not independent business state.

## Build layout

```text
apps/server/                 # sole startup application
modules/
  concepts/<name>/           # one build unit per concept
    CONCEPT.md
    src/
  composition/               # application interfaces and coordination
    SYNCS.md
    src/
      syncs/                 # named rules; not another build unit
  api/                       # protocol, DTO, and error mapping
  shared/                    # passive types
```

`composition` names the module, `syncs` its rules, and `sync` one rule. Keep one SYNCS at the module root,
grouped by entry or responsibility. Adapt source paths to the language, such as Java's composition.syncs package.

Each module has a manifest, public interface, and build/test entry. Targeted builds include declared
dependencies; separate builds do not imply separate startup/deployment. Groups aid navigation and
are not automatically build units. Deliver single-module tasks without an unrelated application skeleton.

## Ports and layers

The code needing a facility declares its contract; an adapter implements it. Server injects adapters
through restricted factories. Test core policies without HTTP, SQL, or a specific scheduler.

| Module | Internal organization |
| --- | --- |
| composition | Named rules and application interfaces; execution ports/recovery adapters as needed |
| concept | Keep simple behavior together; use domain/application/adapter when responsibilities differ |
| api | Inbound adapters; add no domain layer without domain responsibilities |

With Clean layers, domain holds models/invariants, application implements actions/queries, and
adapters implement facilities. Dependencies point inward. Do not add empty layers, forwarding wrappers,
or duplicate ports around existing interfaces. Internal layers use packages/directories rather than
separate build units. Existing confirmed conventions take precedence; these defaults do not authorize migration.

## Example and checks

For a confirmed reservation/payment contract:

```text
request completion → Reservation.hold
hold[Held]         → Payment.charge
charge[Paid]       → Reservation.confirm
charge[Declined]   → Reservation.cancel
```

Match flow and reservation identity, respond after the relevant completion, and retain pending
cancellation on failure. Follow [execution and recovery](execution.md) for exact obligations.

| Prefer | Avoid |
| --- | --- |
| Check manifests and source access. | Treat folders or an acyclic graph as proof of every boundary. |
| Coordinate through named rules. | Let controllers coordinate concepts or concepts call one another. |
| Expose restricted assembly factories. | Open every implementation package for wiring. |
| Test refusal, partial completion, and retry. | Treat exception propagation as recovery. |

Verify builds, public interfaces, applicable layers, concept invariants/operational principles, rules,
and application scenarios. Static checks alone do not establish behavior.
