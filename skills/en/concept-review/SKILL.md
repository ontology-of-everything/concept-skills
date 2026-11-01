---
name: concept-review
description: "Use when explicitly invoked to assess a concept design or compare code with specifications. Perform a read-only review of purpose, independence, and synchronization composition. Use evidence to distinguish design defects, specification issues, and implementation deviations."
metadata:
  language: en
  translation_of: concept-review-cn
  openclaw:
    homepage: https://github.com/ontology-of-everything/concept-skills
---

# Review concept designs

## Goal

Determine whether concept and application designs meet their purposes, and whether available code
conforms. Run only on explicit `$concept-review` invocation. Remain read-only.
Review design without code; without specifications, limit conclusions to observable code properties.

## Principles

Remain read-only. Support findings with inspected requirements, specifications, code, or tests;
label inference and gaps. Without implementation, do not report implementation violations.
Missing tests for an operational principle are verification gaps; a failed purpose argument needs a counterexample.

Check confirmed engineering conventions. Report architecture deviations separately from concept
defects, without imposing a new project skeleton.

## Concepts

| Dimension | Question |
| --- | --- |
| Fitness | Does the behavior meet the real need under stated assumptions? |
| Independence | Can each concept be understood independently, and do concept modules avoid mutual references? |
| Composition | Do synchronizations respect concept contracts and support application scenarios? |
| Drift | Where does implementation omit or contradict the confirmed contract? |
| Product subsets | Does each requested subset retain its purpose, entries, rules, and resources? |

A concept argument connects its contract, operational principle, and purpose. An application argument
connects selection and rules to scenarios and purpose. Successful local tests do not establish
application fitness. Synchronization may restrict behavior while remaining within the contract.

## Workflow

1. Read [the specification contract](references/spec-format.md), requirements, indexes, and relevant
   specifications. Record scope, versions, and gaps; trace available code.
2. Review purpose fulfillment, single purpose, complete behavior, independence, and familiarity for
   the actual user, including API programmers. Novelty alone is not a defect.
3. With code, use [drift checks](references/drift-checklist.md) for interfaces, state, invariants,
   dependencies, private access, shared mutable state, and leaked protocol types.
4. Use [composition checks](references/composition-checklist.md) for legal scenarios, triggers,
   bindings, isolation, failures, replay, loops, and missing/excessive automation.
5. Verify each requested product subset's requirement-based dependencies, entries, rules, resources,
   and build support. Reconcile references and diagrams, then merge findings by root cause.

Read [sources](references/sources.md) to verify definitions. Static reasoning does not prove runtime conformance.

## Examples

| Prefer | Avoid |
| --- | --- |
| Show how a decline leaves a held reservation unreleased, with the rule and reachable path. | Report a long flow as a defect without a failing scenario. |

## Report and completion

Report scope, coverage, severity, and unverified items across the dimensions above. Each finding
states a scenario, current evidence location, failed relation or assumption, impact, and repair step.
Medium-or-higher findings need specification/code evidence; under/over-sync needs a concrete scenario.

Route model defects to design, transcription/index errors to PRD, and code violations to build.
Separate current repairs from later dependencies. Report only executed checks as passed; change no
specifications, code, or history.
