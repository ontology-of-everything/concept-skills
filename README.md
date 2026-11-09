# concept-skills

**Give functionality boundaries. Make coordination visible.**

Adding a share feature can touch posting, authorization, and notification code.
When the connections are scattered, the effects of a change are hard to see.

`concept-design` supports software design and AI coding with Daniel Jackson's concepts and synchronizations.
Start from a user's need, define independent modules and explicit coordination rules, then use them for specifications, implementation, review, and Mermaid maps.
Adapts ideas from WYSIWID (Meng & Jackson, MIT).

## 🧩 How it works

- **Concepts** provide independent functionality with their own state and actions; concepts do not call one another or read one another's state.
- **Synchronizations** make coordination explicit: what happened, which conditions hold, and which actions follow.
- **LLMs and the CLI** have separate roles: an LLM generates or changes code from specifications, the CLI checks specification structure, and review and tests check behavior.

For example: comment created → query the post's author → send a notification.
The synchronization holds the coordination; Comment need not depend on Notification.

## ✨ What it helps with

Locate functionality, change concepts independently, and read coordination rules directly.
Before adding a feature, consider reusing concepts or changing a few synchronizations, then check that existing behavior is preserved.
The goal is more modular, transparent, and understandable software.
See [references](skills/en/concept-design/references/shared/learning/sources.md) for the concept and synchronization methods used by this skill.

## Get started

From this repository, install one language edition:

```sh
npx --yes skills add . --skill concept-design --agent codex --copy --yes
npx --yes skills add . --skill concept-design-cn --agent codex --copy --yes
```

Invoke explicitly; only the workflow needed for the task is read:

```text
$concept-design design Define concepts and synchronizations for reservations.
$concept-design build Implement the confirmed specifications.
$concept-design review src/orders Inspect concept boundaries and code, read-only.
$concept-design guard map src Generate a concept and synchronization diagram.
```

Also supports settle, prd, guard, refine, and explain; Chinese uses `$concept-design-cn`.

## What concept-lint checks

Read-only, with no third-party dependencies. Checks the skill's local [CONCEPT/SYNCS notation](skills/en/concept-design/references/shared/model/spec-format.md):

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
See the [map format](skills/en/concept-design/references/shared/artifacts/map-format.md).

## Repository skills

4R architecture documentation, data semantics, personal knowledge management, and learning have separate skills; each has English and Chinese editions.

`architect-4r` uses Li Yunhua's 4R method to describe existing architecture from code or discussion context. Select views and key scenarios, then see the architecture and how its roles work together. The Chinese edition is `architect-4r-cn`.

```sh
npx --yes skills add . --skill architect-4r --agent codex --copy --yes
npx --yes skills add . --skill architect-4r-cn --agent codex --copy --yes
```

<!-- skill-catalog:start -->

| Skill | Purpose | Version |
| --- | --- | --- |
| [Concept design](skills/en/concept-design/SKILL.md) | Define independent functionality with concepts and coordinate them with synchronization rules. | 2.0.3 |
| [Data Knowledge Architect](skills/en/data-knowledge-architect/SKILL.md) | Model the business meaning of data, facts, dimensions, and relations. | 1.1.0 |
| [Personal Knowledge Architect](skills/en/personal-knowledge-architect/SKILL.md) | Extract, connect, organize, and reuse knowledge from source material. | 0.4.0 |
| [Read It. Reframe It. Own It.](skills/en/read-it-reframe-it-own-it/SKILL.md) | Build and revise understanding around a learning goal and a key framework. | 0.2.0 |
| [4R System Modeling Framework](skills/en/architect-4r/SKILL.md) | Core concepts, definitions, principles, and common mistakes in software architecture models. | 0.4.0 |
| [C4 Software Architecture Model](skills/en/architect-4c/SKILL.md) | Core concepts, definitions, principles, and common mistakes in software architecture models. | 0.1.0 |

<!-- skill-catalog:end -->

## Maintenance and license

The former eight concept-design workflows share one entry per language. Current concept-design version: **2.0.3**. Repository version: **3.1.1**.
Old ClawHub entries redirect to the matching language edition where possible; the rest are retired or already unavailable. Preserve project specifications, code, and user configuration during migration.

Run `./tools/validate-all.sh` to check public packages.
[Repository rules](CLAUDE.md) · [Changes](CHANGELOG.md) · [中文](README-CN.md).
[Apache-2.0](LICENSE). ClawHub bundles use MIT-0.
