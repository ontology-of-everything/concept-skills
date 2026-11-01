---
name: software-concept-architect-guardrails
description: "Validates and maintains concept specifications. Use when explicitly invoked for audit, concept, drift, pipeline, sync, or map."
compatibility: "Read/write/search files; optional Claude Code hooks need bash and jq."
metadata:
  language: en
  translation_of: software-concept-architect-guardrails-cn
  author: ontology-of-everything
  version: "1.1.1"
  openclaw:
    homepage: https://github.com/ontology-of-everything/concept-skills
---

# Software concept architect · guardrails

## Goal

Maintain specifications that describe contracts and can be checked against implementation.
Run only on explicit `$software-concept-architect-guardrails` invocation. The workflow adapts
[wyx v0.26.0](https://github.com/jlifyio/wyx); retain `LICENSE.upstream` and use this repository's notation.

## Principles

Separate facts, inferred purposes, proposals, and open decisions. Report defects without turning
them into valid contracts. Synchronizations respect concept contracts; requirements establish
product dependencies.

Keep one authoritative file per element. Colocate concept-owned PIPELINE with CONCEPT, place
cross-concept pipelines in composition, and group flows in one SYNCS per composition module.
Build units do not automatically qualify as concepts.

Audit and drift change no specifications or code; save scan history only when requested.
Discovery lists candidates. Complete authorized creation/repair in its writing mode. Preserve human
notes and legacy behavior; confirm only unresolved model choices or expanded scope.

## Concepts

| Artifact | Responsibility |
| --- | --- |
| CONCEPT | A concept's purpose, state, actions, and operational principle |
| SYNCS | Application instances, type bindings, and causal synchronization rules |
| PIPELINE | Data sources, transformations, quality rules, and allowed reads and writes |
| ARCHITECTURE | Navigation derived from specifications; it is not an authoritative contract |

Backfill reconstructs contracts from inspected implementation. Drift compares implementation with
confirmed contracts. Neither establishes whether the design meets the user's need.

## Workflow

1. Read project conventions, the PRD index, and relevant specifications. Choose one mode below;
   start with audit when specifications or the mode are missing.
2. For writing modes, a path identifies implementation to inspect; a description proposes behavior.
   No target means candidate discovery only.
3. Read the mode reference. Before writing CONCEPT/SYNCS or checking pipeline interfaces, read
   [the specification contract](references/spec-format.md).
4. Perform checks or authorized edits. Update indexes and rebuild affected maps from content.

| Mode | Output and required reference |
| --- | --- |
| `audit` | [Coverage and repair plan](references/audit.md) |
| `concept` | [Candidates or CONCEPT](references/concept.md) |
| `drift` | [Comparison report](references/drift-detection.md) |
| `pipeline` | [Candidates or PIPELINE](references/pipeline.md) |
| `sync` | [Candidates or SYNCS](references/sync.md) |
| `map` | [Derived maps](references/map.md) |

Read [hook installation](references/hooks-runtime.md) only when requested. Hooks locate specifications
and warn about possible stale maps; they do not verify behavior.

## Examples

| Prefer | Avoid |
| --- | --- |
| Audit classifies a protocol adapter as support code and records the reason. | Create CONCEPT for every build module or change files during an audit. |

## Completion

State scope, evidence, unresolved references, and unverified items. Backfill labels inference;
maps resolve to current specifications. Route model choices to design, confirmed-model transcription
to PRD, and purpose/composition review to review. Describe the work if a companion skill is unavailable.
