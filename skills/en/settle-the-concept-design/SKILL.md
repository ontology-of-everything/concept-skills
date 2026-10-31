---
name: settle-the-concept-design
description: >-
  Use only when the user explicitly requests this skill. Consolidate the full discussion into a concept design for user confirmation, using progressive disclosure and decision matrices to clarify business goals, concepts, composition, tradeoffs, and unresolved issues.
metadata:
  language: en
  translation_of: settle-the-concept-design-cn
  version: "0.1.1"
---

# Settle the Concept Design

Based on [Daniel Jackson's concept design](https://arxiv.org/html/2606.27258v1#S12), consolidate the discussion into business goals, application scope, and design tradeoffs, producing a proposal for confirmation.

Present the concept overview, key scenarios, and necessary specifications in that order, using a decision matrix to record choices, rationale, impact, and confirmation status, prioritizing design changes and details that affect decisions.

Define concepts around independent, complete functional responsibilities, specifying their names, purposes, operational principles (OPs) showing how those purposes are fulfilled, states, and actions with inputs, outputs, preconditions, and effects.

Compose concepts through external causal synchronization rules that coordinate actions, specifying type bindings, triggering actions and state conditions, subsequent actions, parameters, and failure handling while preserving concept behavioral contracts, and use business scenarios to check the composition's observable outcomes, contribution to goals, and underlying assumptions to derive acceptance criteria.

Use consistent terminology, retain decisions and the rationale for revisions, distinguish confirmed, awaiting confirmation, rejected, and unresolved items, label new options, inferences, and missing information as proposals, assumptions, and gaps respectively, and use the design as the basis for subsequent work once confirmed.
