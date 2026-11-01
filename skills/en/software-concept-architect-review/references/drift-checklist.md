# Specification drift and severity

Read specifications with current implementation, migrations/schema, tests, and PRD-staged files.
Use [the contract](spec-format.md) for legacy notation, signatures, cardinality, result cases,
state reads, and reachable matching. Queries have no completion events.

A missing operational-principle test is a verification gap; a failed purpose argument needs a
counterexample. Without code, make no implementation or test-coverage conclusion.

## Categories

| Object/category | Decision rule | Default |
| --- | --- | --- |
| Missing action | public action is undeclared | Medium |
| Removed action | declared action is absent from all relevant implementations | High |
| Changed signature | inputs, real outputs, or error cases changed | Medium |
| New state | undeclared state changes observable behavior | Medium |
| Naming violation | a core concept section depends on another concept definition | Medium |
| Boundary violation | code bypasses another concept's public interface for private state | High |
| Intrinsic coupling | a concept directly calls another concept | High |
| Cross-cutting parameter | a contract-relevant common parameter is undocumented | Medium |
| OP without test | no behavior test covers the representative story | Medium |
| Excluded action used | an application-excluded action is reachable | High |
| Missing/removed sync | coordination is undocumented or a declared rule has no implementation | Medium/High |
| Changed trigger | actual completion differs from `when` | Medium |
| Changed binding/effect | `where` qualification/binding or `then` target/arguments changed | High |
| New participant | actual participating concept is undeclared | High |
| Graph inconsistency | a derived graph differs from its rules | Medium |
| Missing reference | sync action/query, signature, or instantiation does not resolve | High |
| Missing participant | internal concept has no specification or index entry | Medium |

Check external-entry parameters, results, and correlation; Requesting needs no synthetic CONCEPT.
For PIPELINE, missing stages/sources default to Medium, contradictory invariants/private access to High.
Sync diagrams may live in the overall PRD alone. Product dependencies need requirement evidence.

## Severity calibration

Critical needs evidence of authorization bypass, data destruction, or core unavailability.
High is a clear violation; Medium an impactful omission; Low local maintenance. Adjust defaults to
reproducible impact and explain why. Low counts alone do not increase severity.

Silence does not prove prohibition. Private helpers, derived caches, behavior-preserving Result/async
wrappers, and naming maps are not drift by themselves. Public abstract-state reads are allowed.
Recorded exceptions retain their scope and consequences; documenting concept calls does not restore independence.

## Evidence and scope

Check confirmed engineering conventions separately from semantic drift. Under the default modular
monolith, verify independent builds/tests, one-process public-factory assembly, api/composition/concept
boundaries, concept independence, and inward dependencies. Folders or an acyclic graph prove neither
source access nor behavior. Do not impose this default on existing projects.

Evidence Medium-or-higher findings with current locations. Search misses do not prove absence;
unread paths stay unverified. Batch related specifications, record passed/found/unverified per
category, reconcile cross-spec references, and merge shared root causes across affected paths.
