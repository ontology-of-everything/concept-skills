---
name: concept-build
description: "Use when explicitly invoked to implement confirmed concept specifications. Follow project conventions to build independent concept modules and synchronization rules. Verify contracts, end-to-end flows, and required failure recovery."
metadata:
  language: en
  translation_of: concept-build-cn
  openclaw:
    homepage: https://github.com/ontology-of-everything/concept-skills
---

# Implement concept models

## Goal

Implement a confirmed concept model, or provide the requested implementation plan.
Run only on explicit `$concept-build` invocation. Use the specifications,
application purpose, scenarios, and confirmed project conventions as input.

## Principles

Default to a modular monolith with independently built and tested modules, assembled by server
into one process. Business calls follow api, composition, then concept interfaces. Keep public
assembly factories separate from business interfaces.

Use ports and adapters. Add Clean layers when domain and application responsibilities need separation.
Do not add empty layers or forwarding wrappers. Honor existing confirmed conventions and scoped migrations.

Preserve concept contracts, permissions, correlation, failures, and exclusions. Keep concept, action,
and parameter meanings consistent across specifications, code, and logs. Leave model gaps open.

## Concepts

| Module | Responsibility |
| --- | --- |
| concept | Own business state and expose actions/queries; use generic or opaque external identities and no concept-to-concept references. |
| composition | Expose application interfaces and coordinate through named syncs, specified in SYNCS. |
| api | Map external protocols and data to composition interfaces. |
| server / shared | Assemble modules / provide passive types with no business dependencies. |

Actions are observable occurrences, including read-only actions. Queries return bindings without
completion events. A request can occur without the requested action following.

## Workflow

1. Read [the specification contract](references/spec-format.md), confirmed model, project conventions,
   and relevant code/tests. Continue work independent of unresolved model choices.
2. Read [engineering architecture](references/architecture.md) when defining boundaries, then only
   [Rust / Axum](references/rust.md), [Java / Spring](references/java-spring.md), or
   [TypeScript](references/typescript.md). Declare build units, APIs, state owners, and assembly.
3. Read [execution and recovery](references/execution.md) before writing rules. Preserve named
   boundaries; choose a mediator or engine for required matching and recovery behavior.
4. Colocate CONCEPT with each concept and SYNCS with each composition module. Group rules by entry
   or responsibility and update PRD indexes. Use [scaling](references/scaling.md) for demonstrated grouping needs.
5. Build/test affected modules and assembly. Check operational principles, invariants, rule branches, application
   scenarios, concurrency, required recovery, and both build and source-access boundaries.

Read [sources](references/sources.md) to distinguish research from repository choices.

## Examples

| Prefer | Avoid |
| --- | --- |
| Keep payment and reservation separate; a named rule connects payment completion to confirmation. | Call payment from inside the reservation concept. |
| Inject a recovery store through a port when retries must survive a restart. | Assume an in-memory listener provides durable recovery. |

## Completion

Specifications and code agree; executions trace to rules and inputs; excluded actions remain
unreachable. For requested subsets, verify purpose, dependencies, entries, rules, resources, and
build flags. Report tests and gaps. Route model defects to design and transcription errors to PRD.
Conformance alone does not establish purpose fulfillment.
