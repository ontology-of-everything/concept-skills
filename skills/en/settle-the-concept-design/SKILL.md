---
name: settle-the-concept-design
description: >-
  Consolidates software concept design discussions into a proposal for user confirmation using Daniel Jackson's concept design. Use only when the user explicitly invokes $settle-the-concept-design to finalize a concept design, reconcile design decisions, or review changes against an agreed design. Covers business goals, scope, concept specifications, synchronization rules, tradeoffs, acceptance criteria, assumptions, and unresolved issues, presented through an overview, scenarios, and decision matrices. Implementation and publication require separate authorization.
metadata:
  language: en
  translation_of: settle-the-concept-design-cn
  version: "0.1.2"
---

# Settle the Concept Design

Based on Daniel Jackson's concept design, consolidate the discussion into business goals, application scope, and design tradeoffs, producing a proposal for confirmation.

Present the concept overview, key scenarios, and necessary specifications in that order, using a decision matrix to record choices, rationale, impact, and confirmation status, prioritizing design changes and details that affect decisions.

Define concepts around independent, complete functional responsibilities, specifying their names, purposes, operational principles (OPs) showing how those purposes are fulfilled, states, and actions with inputs, outputs, preconditions, and effects.

Compose concepts through external causal synchronization rules that coordinate actions, specifying type bindings, triggering actions and state conditions, subsequent actions, parameters, and failure handling while preserving concept behavioral contracts, and use business scenarios to check the composition's observable outcomes, contribution to goals, and underlying assumptions to derive acceptance criteria.

Use consistent terminology, retain decisions and the rationale for revisions, distinguish confirmed, awaiting confirmation, rejected, and unresolved items, label new options, inferences, and missing information as proposals, assumptions, and gaps respectively, and use the design as the basis for subsequent work once confirmed.
