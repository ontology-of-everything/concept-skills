# concept-skills

[![skills.sh](https://skills.sh/b/ontology-of-everything/concept-skills)](https://skills.sh/ontology-of-everything/concept-skills)

> Name the meaning first — then write code, run a CLI, or draft a spec.

[concept-skills](https://github.com/ontology-of-everything/concept-skills) provides eleven
capabilities as 22 localized [Agent Skills](https://agentskills.io/) for ontology, semantic layers,
concept design, and visual learning. English uses the base name;
Simplified Chinese adds `-cn`.

Cloud operational skills now live in
[`concept-git/cloud-concept-skills`](https://github.com/concept-git/cloud-concept-skills) and are no
longer distributed from this repository.

Office-focused skills now live in the sibling `myoffice-skills` repository and are no longer
distributed from this repository.

The concept-design skills adapt Daniel Jackson's concepts-and-synchronizations model —
[The Essence of Software](https://essenceofsoftware.com/) (2021), with the current when/where/then
sync notation from _Beyond Objects_ ([arXiv:2606.27258](https://arxiv.org/abs/2606.27258)) — for
agent use; an adaptation, not endorsed by the author.

中文说明见 [README-CN.md](README-CN.md).

Current release is **2.7.0**. The concept design workflow, `show-me-the-design`, and `settle-the-concept-design` are explicit-only;
`read-it-reframe-it-own-it` supports automatic discovery; all concept skills require explicit invocation in Codex;
`concept-guard` modes
consume Jackson notation only.

## Table of Contents

- [Skills](#skills)
- [Install](#install)
- [Usage](#usage)
- [Classic usage examples](#classic-usage-examples)
- [Contributing](#contributing)
- [Changelog](CHANGELOG.md)
- [License](#license)

## Skills

<!-- skill-catalog:start -->

Classified by the primary problem each skill solves; family names identify the series.

### Concept Design

Design software concepts, responsibilities, specifications, and implementations.

| Skill | Version | ClawHub category |
| --- | --- | --- |
| [Settle the Concept Design](skills/en/settle-the-concept-design/SKILL.md) | 0.1.4 | development, knowledge |
| [Concept design](skills/en/concept-design/SKILL.md) | 1.0.1 | development |
| [Concept PRD](skills/en/concept-prd/SKILL.md) | 1.1.1 | development |
| [Concept build](skills/en/concept-build/SKILL.md) | 1.1.1 | development |
| [Concept review](skills/en/concept-review/SKILL.md) | 1.1.1 | development |
| [Concept guard](skills/en/concept-guard/SKILL.md) | 1.1.1 | development |
| [Concept refine](skills/en/concept-refine/SKILL.md) | 1.0.1 | development |
| [ShowMeTheDesign](skills/en/show-me-the-design/SKILL.md) | 0.2.1 | knowledge |

### Semantic Modeling

Model the business meaning of data, facts, dimensions, and relations.

| Skill | Version | ClawHub category |
| --- | --- | --- |
| [Data Knowledge Architect](skills/en/data-knowledge-architect/SKILL.md) | 1.1.0 | knowledge |

### Knowledge Management

Extract, connect, organize, and reuse knowledge from source material.

| Skill | Version | ClawHub category |
| --- | --- | --- |
| [Personal Knowledge Architect](skills/en/personal-knowledge-architect/SKILL.md) | 0.4.0 | knowledge |

### Learning Methods

Build and revise understanding around a learning goal and a key framework.

| Skill | Version | ClawHub category |
| --- | --- | --- |
| [Read It. Reframe It. Own It.](skills/en/read-it-reframe-it-own-it/SKILL.md) | 0.2.0 | knowledge |

<!-- skill-catalog:end -->

### Concept design workflow

Purpose-Driven Software Design. Based on Daniel Jackson’s concept design approach in _The Essence of Software_.

Requirements to modules, with the concept model as the contract. Each skill stops at its own
boundary and hands off: `design` → `prd` / `build` → `review`.

Shared principle: synchronization may restrict behavior, never extend a concept contract. Check
contract conformance and purpose fulfillment separately.

Per-skill details and taxonomy: [catalog.yml](catalog.yml).
Localization and directory rules: [CLAUDE.md](CLAUDE.md).

## Install

Requires Node.js 22.20+ and Git. Copy a command below and run it from your project directory. These commands install to Codex in the current project.

Use `--agent claude-code` or `--agent cursor` for another agent; add `--global` to install across projects. See the [installer options](https://github.com/vercel-labs/skills/blob/main/docs/commands.md).

### English editions

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill data-knowledge-architect personal-knowledge-architect concept-design concept-prd concept-build concept-review concept-guard concept-refine read-it-reframe-it-own-it show-me-the-design settle-the-concept-design --agent codex --copy --yes
```

### Simplified Chinese editions

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill data-knowledge-architect-cn personal-knowledge-architect-cn concept-design-cn concept-prd-cn concept-build-cn concept-review-cn concept-guard-cn concept-refine-cn read-it-reframe-it-own-it-cn show-me-the-design-cn settle-the-concept-design-cn --agent codex --copy --yes
```

### Install one skill

**`data-knowledge-architect`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill data-knowledge-architect --agent codex --copy --yes
```

**`personal-knowledge-architect`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill personal-knowledge-architect --agent codex --copy --yes
```

**`concept-design`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill concept-design --agent codex --copy --yes
```

**`concept-prd`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill concept-prd --agent codex --copy --yes
```

**`concept-build`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill concept-build --agent codex --copy --yes
```

**`concept-review`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill concept-review --agent codex --copy --yes
```

**`concept-guard`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill concept-guard --agent codex --copy --yes
```

**`concept-refine`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill concept-refine --agent codex --copy --yes
```

**`read-it-reframe-it-own-it`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill read-it-reframe-it-own-it --agent codex --copy --yes
```

**`show-me-the-design`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill show-me-the-design --agent codex --copy --yes
```

### List available skills

```bash
npx --yes skills add ontology-of-everything/concept-skills --list
```

English payloads live in `skills/en/`; Simplified Chinese payloads live in `skills/zh-CN/` and keep the `-cn` skill names. ClawHub publishes English editions only.

## Usage

Skills normally activate from their description, so plain requests are enough. The
concept design workflow is explicit-only and must be named (`/concept-design` in Cursor,
`$concept-design` in Codex):

```text
$concept-design model this requirement as independent concepts
$concept-prd transcribe the confirmed model into a PRD
$concept-guard drift src/orders
$show-me-the-design explain this concept model with a small diagram
Turn this API into a semantic layer                 → data-knowledge-architect
```

To pin a skill explicitly: `/skill-name` in Cursor, `$skill-name` in Codex.

## Classic usage examples

Each skill has two examples. Install it, share the relevant material, then copy a request.
Replace example paths with your project paths.

### Settle the Concept Design

`settle-the-concept-design` · [Skill](skills/en/settle-the-concept-design/SKILL.md)

Based on Daniel Jackson's concept design, consolidate discussion into decisions for confirmation, from goals and concept purposes to scenarios and the specifications needed for those decisions.

| Scenario | Try saying |
| --- | --- |
| Settle a design | `$settle-the-concept-design` Consolidate our discussion into a concept design; show the choices, rationale, and unresolved issues for confirmation. |
| Revisit decisions | `$settle-the-concept-design` Compare this round with our confirmed design; show what changed, why, and how it affects business goals and acceptance criteria. |

### Read It. Reframe It. Own It

`read-it-reframe-it-own-it`

| Scenario | Try saying |
| --- | --- |
| Organize notes | `$read-it-reframe-it-own-it` Turn these concept-design notes into a knowledge tree I can use for revision. |
| Make a study sketchnote | `$read-it-reframe-it-own-it` Turn this knowledge tree into a Chinese study sketchnote. |

The second example also needs an image-generation tool. [The English skill is on ClawHub](https://clawhub.ai/agenticweb4/skills/learning-read-it-reframe-it-own-it);
its marketplace URL uses a different slug from the repository installation name.

### ShowMeTheDesign

`show-me-the-design` · [Usage and visual toolbox](skills/en/show-me-the-design/SKILL.md)

Help beginners understand and examine software concepts and how they work together, from overview to detail, using source evidence and visuals. The bundled design reference provides reusable HTML, CSS, and JavaScript.

| Scenario | Try saying |
| --- | --- |
| Understand a design | `$show-me-the-design` Explore this project and visualize concept boundaries and coordinated actions. |
| Check implementation | `$show-me-the-design` Compare this design with source and explain differences and their effects. |

### Personal Knowledge Architect

`personal-knowledge-architect`

| Scenario | Try saying |
| --- | --- |
| Find reusable methods | `$personal-knowledge-architect` Pull out reusable methods from these interview notes. Show me the outline first. |
| Build a method library | `$personal-knowledge-architect` Turn these product-research notes into a method library and merge duplicates. |

### Data Knowledge Architect

`data-knowledge-architect`

| Scenario | Try saying |
| --- | --- |
| Understand a table | `$data-knowledge-architect` Which parts of this order table are facts, dimensions, and measures? |
| Model APIs | `$data-knowledge-architect` Build a semantic model from these order APIs. Export OKF after we confirm it. |

### Software Concept Architect · Design

`concept-design`

| Scenario | Try saying |
| --- | --- |
| Design a task list | `$concept-design` Help me design a task list that supports adding, completing, and reopening tasks. |
| Design reservations | `$concept-design` When a restaurant is full, customers can join a waiting list. What concepts do we need, and how do they work together? |

### Software Concept Architect · PRD

`concept-prd`

| Scenario | Try saying |
| --- | --- |
| Write a PRD | `$concept-prd` Turn our confirmed task-list model into a short PRD. |
| Write specifications | `$concept-prd` Write CONCEPT.md and SYNCS.md for this reservation system using our confirmed design. |

### Software Concept Architect · Build

`concept-build`

| Scenario | Try saying |
| --- | --- |
| Build a task list | `$concept-build` Build our confirmed task-list model in TypeScript and test it. |
| Build reservations | `$concept-build` Implement reservations and cancellations from these specs, then check the flow. |

### Software Concept Architect · Review

`concept-review`

| Scenario | Try saying |
| --- | --- |
| Review a model | `$concept-review` Check this task-list model for problems. Leave it unchanged for now. |
| Compare code with specs | `$concept-review` Check the reservation code against its specs and show me where they differ. |

### Software Concept Architect · Guardrails

`concept-guard`

| Scenario | Try saying |
| --- | --- |
| Find missing specs | `$concept-guard` audit src/reservations Which specs are missing here? List them for me. |
| Check drift | `$concept-guard` drift src Check whether the code matches its specs. Report only. |

### Software Concept Architect · Refine

`concept-refine`

| Scenario | Try saying |
| --- | --- |
| Check responsibilities | `$concept-refine` This Todo handles tasks and sends reminders. Should we split it? |
| Compare similar concepts | `$concept-refine` Should Favorites and Read Later stay separate? Walk me through the use cases. |

**A connected workflow:** design and confirm the model → PRD → implementation → review. For an existing project, start with Guardrails audit, then backfill specifications or refine concepts as needed.

Use `show-me-the-design` at any step to explain the current model or implementation visually.

## Contributing

`qa/` is private and untracked; public checks do not depend on it. Run `./tools/validate-all.sh --local-qa` only when local QA is available.

Project rules and repository ownership: [CLAUDE.md](CLAUDE.md).

```bash
git config core.hooksPath .githooks
./tools/validate-all.sh
```

`skills/en/<name>/` and `skills/zh-CN/<name>-cn/` are self-contained install payloads. QA stays private and untracked. Update both locales, the public catalog, README views, and parity checks together.

## License

[Apache-2.0](LICENSE) © concept-skills contributors. Bundles published to
[ClawHub](https://clawhub.ai/) are MIT-0 there; the repository source stays Apache-2.0.
