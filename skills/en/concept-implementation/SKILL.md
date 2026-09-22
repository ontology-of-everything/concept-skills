---
name: concept-implementation
description:
  Implements a confirmed concept model as a modular monolith only when the user explicitly invokes
  $concept-implementation. Use to map concepts to independent modules, implement synchronization
  composition, colocate specifications, and verify behavioral and dependency contracts.
metadata:
  language: en
  translation_of: concept-implementation-cn
  openclaw:
    homepage: https://github.com/ontology-of-everything/concept-skills/tree/main/skills/en/concept-implementation
---

# Concept Implementation

Focus: how should confirmed concept behavior become verifiable, composable modules? Run only on
explicit `$concept-implementation` invocation. Deliver a plan or code as requested. Continue
confirmed portions and route model gaps that affect implementation back to `concept-design`.

A concept module encapsulates state, invariants, actions, and queries. Modules do not reference one
another. Ports declare interfaces and adapters implement them; domain code depends on neither
protocols nor other concepts. The synchronization layer coordinates public actions and owns
cross-concept policy; the composition root wires implementations, while interface adapters translate
DTOs and protocols into composition entry points.

**Synchronization may restrict behavior, never extend the contract**: composition invokes allowed
behavior; concept actions enforce preconditions, invariants, effects, and result cases. Queries
cannot replace atomic checks. OPs test concept purposes, end-to-end scenarios application purpose;
conformance alone does not establish fitness. Route evidenced purpose failures back to the model.

## Constraints

- Public interfaces, including queries, preserve confirmed coordination and authorization policy;
  one entry point may trigger multiple rules.
- The composition layer owns no domain state, but may persist provenance, retry, and idempotency
  records.
- Errors are matchable output cases with an explicit response, retry, compensation, or
  intentional-ignore strategy. Transactions do not replace failure semantics.
- Change the specification before implementing confirmed new behavior. Grouping exists only to solve
  navigation, build, or team pain.

## Implement and Verify

1. **Verify input** — Read `references/spec-format.md`, application purpose, concept model, both
   argument layers, colocated or staged specifications, and project conventions. Trace actions,
   persistence, failure paths, and tests in existing code. Route model defects to design,
   transcription errors to PRD, and code violations here.
2. **Map modules** — Map each concept to one testable module. Prefer a separate package without
   requiring it. Keep physical state private, expose abstract state for composition queries, and
   expose actions as services. Preserve declared query bindings. Implement zero or more type
   parameters as generics or opaque IDs, never another concept's entity type.
3. **Implement composition** — Read `references/composition-layer.md`; default to a mediator and
   consider an engine only for evolving rules, multi-event matching, or tracing. Preserve completion
   events, bindings, concurrency, request correlation, and failure semantics. Interface adapters map
   requests or messages to explicit entry points; coordination produces required responses.
4. **Colocate specifications** — Place CONCEPT with its module and SYNCS with its composition
   package; migrate staged files and update the overall PRD index.
5. **Verify behavior and seams** — Read only the applicable language reference and add architectural
   guardrails to CI. Tie OP tests to concept purposes and end-to-end tests to application purpose
   and synchronizations, including assumptions. Verify each concept's composed behavior sequences
   against its contract. Read `references/scaling.md` only when
   grouping or package splitting solves observed pain.

Completion requires no concept-module references, all cross-concept business policy in
synchronizations, protected domain seams in CI, contract tests for OPs, application scenarios,
invariants, bindings, match cardinality, failure, replay, and request isolation, observable
completion semantics through transactions, colocated specifications matching code, excluded actions
neither called nor exposed, and product subsets verified against dependency closure, entry points,
remaining rules, resources, and build flags.

Language references: Rust `references/rust.md`; Spring Modulith `references/java-spring.md`;
TypeScript `references/typescript.md`; engineering sources `references/sources.md`.
