---
name: show-me-the-design
description: "Use when explicitly requested to understand software concepts, design tradeoffs, or collaboration flows. Select the diagrams and examples needed from code and specifications, distinguishing facts, inferences, and unverified details."
metadata:
  language: en
  translation_of: show-me-the-design-cn
  version: "0.2.2"
---

# Explain software concepts visually

## Goal

Explain software concepts through visuals grounded in source code. Run only when the user explicitly
requests this skill. Start with the reader's question and a project scenario; explain unfamiliar terms
through examples before naming them.

## Principles

Inspect relevant entries, state, actions, callers, UI queries, configuration, tests, and failures.
Cite files, symbols, and current lines. Documents express intent; code establishes implementation.
A class or file does not automatically establish a concept. Label conflicts, inference, and unknowns.
Without source, explain only the supplied design.

Choose the smallest useful view and keep project terms consistent. Teaching order and simulations
do not prove execution order, transactions, or runtime behavior. Separate current facts from proposals.
Claim checks and previews only when performed.

## Concepts

A concept provides value through state and actions. Its operational principle, or OP, explains a
typical useful result. Synchronizations coordinate independent concepts. Distinguish state relations,
type bindings, instances, product dependencies, and runtime calls.

## Workflow

1. Establish purpose, scenario, reader question, and evidence. Trace relevant code before selecting a view.
2. Read [views and notation](references/views.md). Start with an overview, follow the scenario,
   and expand only the required state, rules, UI mapping, or implementation.
3. Pair visuals with causal explanations and source. Keep details connected to the overview.
4. Before authoring HTML, interactions, or courses, read [the design language](references/design-system.md)
   and reuse its CSS/JavaScript. Show proposed changes with evidence, benefits, and costs.
5. Check the explanation and proposed design against source and concept criteria.

## Examples

| Prefer | Avoid |
| --- | --- |
| Draw both required completions into one rule node and label the query separately. | Draw a serial call chain when the source only proves rule participation. |

## Completion

The reader can locate the scenario, follow its behavior, and inspect the evidence. State omissions
and unknowns. Check the delivered artifact's navigation, selection, comparison, reset, keyboard access,
and narrow layout; reset changes simulation state only.

Deliver courses as an assembled offline directory with shared styles/scripts, separately maintained
sections, and local assets. Open and inspect the result without remote resources, module fetches,
installation, or a server.
