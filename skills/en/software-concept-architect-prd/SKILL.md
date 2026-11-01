---
name: software-concept-architect-prd
description: "Generates PRD and specification files. Use when explicitly invoked to document a confirmed concept model and its acceptance criteria."
metadata:
  language: en
  translation_of: software-concept-architect-prd-cn
  openclaw:
    homepage: https://github.com/ontology-of-everything/concept-skills
---

# Software concept architect · PRD

## Goal

Write a confirmed model into a PRD and specification files without changing its meaning.
Run only on explicit `$software-concept-architect-prd` invocation. Use the confirmed concepts,
synchronizations, dependencies, exclusions, and open decisions as input.

## Principles

Transcribe confirmed behavior without redesigning it. Do not infer requirements from code differences
or fill model gaps. Synchronizations must stay within concept contracts. Preserve assumptions,
human notes, rejected options, and confirmation status.

## Concepts

| File | Responsibility |
| --- | --- |
| Overall PRD | Application purpose, scenarios, indexes, dependencies, subsets, exclusions, and open decisions |
| CONCEPT | A concept's purpose, state, actions, and operational principle, or OP |
| SYNCS | Application instances, type bindings, and synchronization rules |

Keep one authoritative location per model element. The concept argument connects its contract,
OP, and purpose. The application argument connects concept selection, rules, scenarios, and purpose.
Acceptance criteria cite the argument or contract they check.

## Workflow

1. Read the confirmed model, requirement sources, and existing documents. Inspect code only to
   locate modules or verify index facts.
2. Use [file layout](references/templates.md) to choose one authoritative location per element.
   Use the staging locations before modules exist; otherwise colocate specifications with
   their concept and composition modules.
3. Write the overall PRD with purpose, scenarios, mismatches, indexes, sync diagram, product
   dependencies, viable subsets, cross-concept assumptions, exclusions, and open decisions.
4. Follow [the specification contract](references/spec-format.md). Keep concept definitions independent,
   application context in notes, type instantiation in SYNCS, and rule groups under `// flow:`.
5. Derive acceptance from OPs, scenarios, and contracts. Preserve failure and empty-query behavior;
   check signatures, bindings, and results. Update indexes and derived diagrams after focused edits.

Use [the reservation example](references/example-reserving.md) for transcription and
[sources](references/sources.md) for notation. Implementation-time moves and module splits belong to build.

## Examples

| Prefer | Avoid |
| --- | --- |
| Keep an unspecified cancellation result open and name the acceptance it blocks. | Invent an error result to complete the template. |

## Completion

Each definition and decision has one location; links and signatures resolve. Acceptance cites its
source, and missing goals remain open. Route model gaps to `software-concept-architect-design`
and implementation to `software-concept-architect-build`. If unavailable, describe the required work.
