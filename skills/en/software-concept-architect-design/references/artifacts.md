# Design artifacts

Confirm the inventory, application scenarios, and product subsets before adding them to the
confirmed record. Keep pending items separate and reuse earlier confirmation.

## Alignment

| Section | Required content |
| --- | --- |
| Concept inventory | Name, purpose, operational principle, familiar/variant/new, user-visible state, confirmation status |
| Application scenarios | Beneficiary, purpose, current and desired behavior, constraints, observable conditions/results, participating concepts and rules, counterexamples |
| Dependencies and subsets | Requirement-backed dependencies, explanation order, viable subsets, minimum product, entries, remaining rules, and external resources |

For each item, distinguish evidence, inference, and unresolved assumptions. Record confirmed or
pending status. `A → B` means retaining A in this product requires B; it is not a code dependency.

## Confirmed record

| Section | Required content |
| --- | --- |
| Concepts | Purpose, state, actions, operational principle, optional queries/notes; reasons for all eight qualification decisions |
| Synchronizations | App/include/sync rules grouped by entry or responsibility and linked to confirmed scenarios |
| Synchronization diagram | Rule nodes with all conjunctive when inputs, then targets, and separate where reads |
| Exclusions and open decisions | Candidate/action/assumption, decision, source, impact, and the work it blocks |

Follow [the specification contract](spec-format.md). Explain how each contract supports its
operational principle and how the result meets the purpose. State gaps instead of implying proof.
Keep the synchronization diagram separate from product dependencies.
