---
name: concept-design
description: "Generates concept designs from software needs. Use when explicitly invoked to define concepts, behavior, and synchronization."
metadata:
  language: en
  translation_of: concept-design-cn
  openclaw:
    homepage: https://github.com/ontology-of-everything/concept-skills
---

# Concept design

## Goal

Turn a software need into a concept design the user can confirm. Run only on explicit
`$concept-design` invocation. Deliver a model and its unresolved decisions.
Continue to PRD or implementation when the user has authorized that work.

## Principles

Use requirements, examples, and inspected code as evidence. Separate facts, proposals, inference,
and open decisions. A page, entity, or file is only a candidate clue.

Check the concept contract, operational principle, and purpose together. Separately check whether concept selection
and synchronization fulfill application scenarios and purpose. One argument does not prove the other.
Apply the single-purpose criterion to concepts.

Reuse confirmed decisions. Confirm only unresolved choices affecting scope or behavior; continue
work independent of them and state what remains blocked.

## Concepts

- A concept has one purpose and its own state and actions. Its definition does not depend on
  another concept. Use a familiar concept or a small variant when it meets the need.
- An operational principle, or OP, describes how typical actions fulfill the concept's purpose.
- A synchronization is an external rule that coordinates concept actions for an application.
  It may restrict behavior but must respect each concept's contract.

## Workflow

1. Establish beneficiaries, application purpose, current behavior, desired outcome, and constraints.
   For existing software, inspect entries, state ownership, failures, and tests.
2. Draft [the inventory and alignment](references/artifacts.md). Confirm included concepts, then use
   [the specification contract](references/spec-format.md) for state and actions. External identities
   are type parameters with no assumed fields.
3. Apply all eight [qualification criteria](references/criteria.md). Record evidence and disputed
   boundaries. Correct demonstrated mismatches between behavior and need.
4. Use [composition checks](references/sync-notation.md) for rules, missing/excessive automation,
   and the sync diagram. Confirm product dependencies and subsets, including purpose, entries,
   remaining rules, and resources.
5. Write confirmed decisions into the record. Keep pending concepts, assumptions, alternatives,
   and their consequences in exclusions and open decisions.

Read [the reservation example](references/example-reserving.md) for a walkthrough and
[sources](references/sources.md) for definitions. Load references only for the current step.

## Examples

| Prefer | Avoid |
| --- | --- |
| Define Comment with a generic target identity; bind it to Post in the application. | Make Comment import Post or read its private state. |
| Explain how reserving and later claiming a slot fulfill a commitment. | Treat creating a database row as the complete reservation purpose. |

## Completion

The record contains confirmed concepts, rules, a sync diagram, exclusions, and open decisions.
Show confirmation status and purpose arguments with their gaps. Required responses cover success
and refusal. The specification and composition checks pass.
