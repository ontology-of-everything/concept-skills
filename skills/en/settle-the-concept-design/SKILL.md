---
name: settle-the-concept-design
description: "Use when explicitly invoked to consolidate a concept-design discussion. Organize goals, options, tradeoffs, consequences, and acceptance criteria. Preserve confirmation status, distinguishing confirmed decisions, suggestions, and unresolved matters."
metadata:
  language: en
  translation_of: settle-the-concept-design-cn
  version: "0.1.5"
---

# Prepare concept proposals

Use Daniel Jackson's concept design to consolidate the discussion into a design proposal for confirmation. Run
only when the user explicitly invokes this skill. Retain confirmed decisions, distinguish proposals,
assumptions, and information gaps, and do not reopen settled matters without new evidence.

Start with business goals, scope, constraints, and changes, then present a concept overview and key scenarios.
Expand details as needed. A concept is a complete functional unit with a clear purpose that can be understood
independently. It includes state, actions, and an operational principle. The operational principle uses a
typical action sequence to explain how the purpose is fulfilled. State expresses facts needed for behavior as
sets and relations. Table records show facts that hold at a particular moment. Actions specify inputs,
outputs, preconditions, and state effects.

Concept composition identifies the concept instances and their type bindings. Synchronization rules sit
outside the concepts and specify triggering actions, state conditions, parameter sources, and requested
subsequent actions. Execution must still satisfy each action's own conditions. Use business scenarios to
explain how the composition supports goals, what assumptions it depends on, and how to assess acceptance. Add
mappings to physical table structures, external interfaces, or services only when they affect the decision.
Distinguish behavioral requirements from implementation choices.

Use a decision matrix to present choices, rationale, impact, acceptance criteria, and confirmation status. Ask
the user to confirm only unresolved matters. Use confirmed results as the basis for subsequent work. Reuse
existing authorization for implementation and publication, and obtain the relevant authorization when it is
missing.
