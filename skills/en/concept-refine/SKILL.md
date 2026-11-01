---
name: concept-refine
description: Analyzes and refines existing software concepts. Use when concept designs need evidence-led refactoring for overload, redundancy, narrowness, fragmentation, or synchronization problems.
metadata:
  language: en
  translation_of: concept-refine-cn
  version: "1.0.1"
---

# Concept refine

## Goal

Correct a demonstrated concept-design problem with the smallest sufficient change. Use the requested
scope, requirements, specifications, and relevant code. A review produces proposals; an authorized
repair includes edits and verification.

## Principles

Inspect evidence, label inferred intent, and retain no change as an option. Preserve confirmed
decisions and concept contracts. Distinguish behavior-preserving code refactoring from intentional
redesign. Local tests alone do not establish application fitness.

## Concepts

A concept has its own purpose, state, actions, and operational principle. Synchronizations coordinate
concepts for application purposes. Suspected overload, redundancy, narrowness, fragmentation, or
coordination problems need a concrete scenario, not a judgment from size or names.

## Workflow

1. Establish the problem, desired outcome, and evidence; inspect affected concepts, rules, callers,
   and tests.
2. Use [moves and evidence](references/moves.md) to compare split/merge, unify/specialize, and
   tighten/loosen against the root cause.
3. Show the recommendation, alternatives, benefit, cost, affected contracts, and behavioral differences.
   Reuse prior authorization; confirm only unresolved consequential choices.
4. Complete authorized edits. Specify confirmed new behavior before implementation, then verify
   invariants, purpose, affected scenarios, and failure paths.

## Examples

| Prefer | Avoid |
| --- | --- |
| Separate authentication from profile editing when evidence shows unrelated purposes. | Split a concept because its file exceeds a chosen line count. |

## Completion

Report preserved and intentionally changed behavior, checks run, regressions, and unknowns.
Finish when the agreed problem is resolved without known major regressions.
