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

The software-concept-architect-design skills adapt Daniel Jackson's concepts-and-synchronizations model —
[The Essence of Software](https://essenceofsoftware.com/) (2021), with the current when/where/then
sync notation from _Beyond Objects_ ([arXiv:2606.27258](https://arxiv.org/abs/2606.27258)) — for
agent use; an adaptation, not endorsed by the author.

中文说明见 [README-CN.md](README-CN.md).

Current release is **2.5.0**. The concept design workflow, `see-the-concept`, and `settle-the-concept-design` are explicit-only;
`software-concept-architect-refine` and `read-it-reframe-it-own-it` support automatic discovery;
`software-concept-architect-guardrails` modes
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
| [Settle the Concept Design](skills/en/settle-the-concept-design/SKILL.md) | 0.1.2 | development, knowledge |
| [Software Concept Architect · Design](skills/en/software-concept-architect-design/SKILL.md) | 1.0.0 | development |
| [Software Concept Architect · PRD](skills/en/software-concept-architect-prd/SKILL.md) | 1.1.0 | development |
| [Software Concept Architect · Build](skills/en/software-concept-architect-build/SKILL.md) | 1.1.0 | development |
| [Software Concept Architect · Review](skills/en/software-concept-architect-review/SKILL.md) | 1.1.0 | development |
| [Software Concept Architect · Guardrails](skills/en/software-concept-architect-guardrails/SKILL.md) | 1.1.0 | development |
| [Software Concept Architect · Refine](skills/en/software-concept-architect-refine/SKILL.md) | 1.0.0 | development |
| [See the Concept](skills/en/see-the-concept/SKILL.md) | 0.1.4 | knowledge |

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
npx --yes skills add ontology-of-everything/concept-skills --skill data-knowledge-architect personal-knowledge-architect software-concept-architect-design software-concept-architect-prd software-concept-architect-build software-concept-architect-review software-concept-architect-guardrails software-concept-architect-refine read-it-reframe-it-own-it see-the-concept settle-the-concept-design --agent codex --copy --yes
```

### Simplified Chinese editions

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill data-knowledge-architect-cn personal-knowledge-architect-cn software-concept-architect-design-cn software-concept-architect-prd-cn software-concept-architect-build-cn software-concept-architect-review-cn software-concept-architect-guardrails-cn software-concept-architect-refine-cn read-it-reframe-it-own-it-cn see-the-concept-cn settle-the-concept-design-cn --agent codex --copy --yes
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

**`software-concept-architect-design`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill software-concept-architect-design --agent codex --copy --yes
```

**`software-concept-architect-prd`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill software-concept-architect-prd --agent codex --copy --yes
```

**`software-concept-architect-build`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill software-concept-architect-build --agent codex --copy --yes
```

**`software-concept-architect-review`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill software-concept-architect-review --agent codex --copy --yes
```

**`software-concept-architect-guardrails`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill software-concept-architect-guardrails --agent codex --copy --yes
```

**`software-concept-architect-refine`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill software-concept-architect-refine --agent codex --copy --yes
```

**`read-it-reframe-it-own-it`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill read-it-reframe-it-own-it --agent codex --copy --yes
```

**`see-the-concept`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill see-the-concept --agent codex --copy --yes
```

### List available skills

```bash
npx --yes skills add ontology-of-everything/concept-skills --list
```

English payloads live in `skills/en/`; Simplified Chinese payloads live in `skills/zh-CN/` and keep the `-cn` skill names. ClawHub publishes English editions only.

## Usage

Skills normally activate from their description, so plain requests are enough. The
concept design workflow is explicit-only and must be named (`/software-concept-architect-design` in Cursor,
`$software-concept-architect-design` in Codex):

```text
$software-concept-architect-design model this requirement as independent concepts
$software-concept-architect-prd transcribe the confirmed model into a PRD
$software-concept-architect-guardrails drift src/orders
$see-the-concept explain this concept model with a small diagram
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

### See the Concept

`see-the-concept` · [Usage and visual toolbox](skills/en/see-the-concept/SKILL.md)

Help beginners understand and examine software concepts and how they work together, from overview to detail, using source evidence and visuals. The bundled design reference provides reusable HTML, CSS, and JavaScript.

| Scenario | Try saying |
| --- | --- |
| Understand a design | `$see-the-concept` Explore this project and visualize concept boundaries and coordinated actions. |
| Check implementation | `$see-the-concept` Compare this design with source and explain differences and their effects. |

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

`software-concept-architect-design`

| Scenario | Try saying |
| --- | --- |
| Design a task list | `$software-concept-architect-design` Help me design a task list that supports adding, completing, and reopening tasks. |
| Design reservations | `$software-concept-architect-design` When a restaurant is full, customers can join a waiting list. What concepts do we need, and how do they work together? |

### Software Concept Architect · PRD

`software-concept-architect-prd`

| Scenario | Try saying |
| --- | --- |
| Write a PRD | `$software-concept-architect-prd` Turn our confirmed task-list model into a short PRD. |
| Write specifications | `$software-concept-architect-prd` Write CONCEPT.md and SYNCS.md for this reservation system using our confirmed design. |

### Software Concept Architect · Build

`software-concept-architect-build`

| Scenario | Try saying |
| --- | --- |
| Build a task list | `$software-concept-architect-build` Build our confirmed task-list model in TypeScript and test it. |
| Build reservations | `$software-concept-architect-build` Implement reservations and cancellations from these specs, then check the flow. |

### Software Concept Architect · Review

`software-concept-architect-review`

| Scenario | Try saying |
| --- | --- |
| Review a model | `$software-concept-architect-review` Check this task-list model for problems. Leave it unchanged for now. |
| Compare code with specs | `$software-concept-architect-review` Check the reservation code against its specs and show me where they differ. |

### Software Concept Architect · Guardrails

`software-concept-architect-guardrails`

| Scenario | Try saying |
| --- | --- |
| Find missing specs | `$software-concept-architect-guardrails` audit src/reservations Which specs are missing here? List them for me. |
| Check drift | `$software-concept-architect-guardrails` drift src Check whether the code matches its specs. Report only. |

### Software Concept Architect · Refine

`software-concept-architect-refine`

| Scenario | Try saying |
| --- | --- |
| Check responsibilities | `$software-concept-architect-refine` This Todo handles tasks and sends reminders. Should we split it? |
| Compare similar concepts | `$software-concept-architect-refine` Should Favorites and Read Later stay separate? Walk me through the use cases. |

**A connected workflow:** design and confirm the model → PRD → implementation → review. For an existing project, start with Guardrails audit, then backfill specifications or refine concepts as needed.

Use `see-the-concept` at any step to explain the current model or implementation visually.

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
