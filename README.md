# concept-skills

**Give functionality boundaries. Make coordination visible.**

Adding a share feature can touch posting, authorization, and notification code.
When the connections are scattered, the effects of a change are hard to see.

`concept-design` supports software design and AI coding with Daniel Jackson's concepts and synchronizations.
Start from a user's need, define independent modules and explicit coordination rules, then use them for specifications, implementation, review, and Mermaid maps.
Specifications follow Beyond Objects (Daniel Jackson); engineering execution draws on WYSIWID (Meng & Jackson).

## How it works

- **Concepts** provide independent functionality with their own state and actions; concepts do not call one another or read one another's state.
- **Synchronizations** make coordination explicit: what happened, which conditions hold, and which actions follow.
- **LLMs and the CLI** have separate roles: an LLM generates or changes code from specifications, the CLI checks specification structure, and review and tests check behavior.

For example: comment created → query the post's author → send a notification.
The synchronization holds the coordination; Comment need not depend on Notification.

## What it helps with

Locate a function, change a concept on its own, and read the coordination rules.
Before adding a feature, reuse a concept or change a few synchronizations, then check that existing behavior still holds.
Methods: [references](skills/en/concept-design/SKILL.md#references).

## Get started

Install from this repository, one language at a time. `--agent claude-code` or `--agent cursor` selects another agent.

```sh
npx --yes skills add . --skill concept-design --agent codex --copy --yes
```

Chinese: the same command with `concept-design-cn`. Invoke by name. The skill reads only the workflow the task needs.

```text
$concept-design design Define concepts and synchronizations for reservations.
$concept-design build Implement the confirmed specifications.
$concept-design review src/orders Inspect concept boundaries and code, read-only.
$concept-design guard map src Generate a concept and synchronization diagram.
```

Also supports settle, prd, guard, refine, and explain; Chinese uses `$concept-design-cn`.

## What concept-lint checks

Read-only, with no third-party dependencies. Checks the skill's local [tool encoding](skills/en/concept-design/references/tool-encoding.md):

```sh
python3 skills/en/concept-design/scripts/concept_lint.py CONCEPT.md SYNCS.md --json
```

Checks declarations and core sections, when/then completion and invocation shapes, top-level named fields, and rule-name uniqueness for each app across the supplied files.
Unknown or legacy call notation is unchecked; types, bindings, concept independence, and runtime results still require other evidence.
Exit codes: `0` passed the listed checks, `1` format error, `2` read/usage error, `3` not checked.

## Generate a concept and synchronization diagram

Scan CONCEPT.md and SYNCS.md to produce one ARCHITECTURE.md with a concept index, Mermaid diagram, relation table, and source lines.
Definitions, instances, and synchronization rules have separate identities; unresolved references remain gaps.

```sh
python3 skills/en/concept-design/scripts/concept_map.py <project-root> --output <project-root>/ARCHITECTURE.md
```

Use `--scope RELPATH` to narrow the view or `--check` to compare without writing. Existing documents retain text outside the generated region.
See the [map format](skills/en/concept-design/references/diagram-contract.md).

## Repository skills

Each skill has an English name and a `-cn` edition. Install with the command above and the skill name. The table below uses one purpose line per domain. These lines name the skill:

| Skill | What it covers |
| --- | --- |
| `data-knowledge-architect` | Business meaning of data, facts, dimensions, and relations. |
| `personal-knowledge-architect` | Methods, scenarios, and entities extracted from source text. |
| `read-it-reframe-it-own-it` | A knowledge tree under one learning goal and one framework. |
| `architect-4r` | Existing architecture from code or discussion, using Li Yunhua's 4R method. |
| `architect-4c` | Simon Brown's C4 model: levels, principles, and common mistakes. |
| `architect-frontend-feature-first` | Feature-first frontends: capability ownership and cross-feature boundaries. |
| `architect-frontend-fsd` | Feature-Sliced Design: layers, slices, segments, public APIs, and dependency boundaries. |
| `agent-dx-cli` | Design, review, and refactor CLIs for agents, scored from executable evidence. |

<!-- skill-catalog:start -->

| Skill | Purpose | Version |
| --- | --- | --- |
| [Java Code Simplification](skills/en/simplify-java/SKILL.md) | Simplify Java / Spring Boot code while preserving behavior and useful boundaries. | 0.2.1 |
| [Concept Modeling Principles](skills/en/concept-model/SKILL.md) | Define independent functionality with concepts and coordinate them with synchronization rules. | 1.1.0 |
| [Concept design](skills/en/concept-design/SKILL.md) | Define independent functionality with concepts and coordinate them with synchronization rules. | 2.5.1 |
| [Data Knowledge Architect](skills/en/data-knowledge-architect/SKILL.md) | Model the business meaning of data, facts, dimensions, and relations. | 1.1.0 |
| [Personal Knowledge Architect](skills/en/personal-knowledge-architect/SKILL.md) | Extract, connect, organize, and reuse knowledge from source material. | 0.4.0 |
| [Read It. Reframe It. Own It.](skills/en/read-it-reframe-it-own-it/SKILL.md) | Build and revise understanding around a learning goal and a key framework. | 0.2.0 |
| [4R System Modeling Framework](skills/en/architect-4r/SKILL.md) | Core concepts, definitions, principles, and common mistakes in software architecture models. | 0.4.0 |
| [C4 Software Architecture Model](skills/en/architect-4c/SKILL.md) | Core concepts, definitions, principles, and common mistakes in software architecture models. | 0.1.0 |
| [Feature-first frontend architecture](skills/en/architect-frontend-feature-first/SKILL.md) | Core concepts, definitions, principles, and common mistakes in software architecture models. | 0.1.0 |
| [Feature-Sliced Design for frontends](skills/en/architect-frontend-fsd/SKILL.md) | Core concepts, definitions, principles, and common mistakes in software architecture models. | 0.1.0 |
| [Agent DX CLI](skills/en/agent-dx-cli/SKILL.md) | Predictable, defensible CLI design, review, and refactoring. | 0.4.2 |

<!-- skill-catalog:end -->

## Maintenance and license

The former eight concept-design workflows share one entry per language. concept-design version: **2.5.1**. Repository version: **3.8.1**.
Old ClawHub entries redirect to the matching language edition where possible; the rest are retired or already unavailable. Preserve project specifications, code, and user configuration during migration.

Run `./tools/validate-all.sh` to check public packages.
[Repository rules](CLAUDE.md) · [Changes](CHANGELOG.md) · [中文](README-CN.md).
[Apache-2.0](LICENSE). ClawHub bundles use MIT-0.
