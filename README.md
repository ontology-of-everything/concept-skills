# concept-skills

[![skills.sh](https://skills.sh/b/ontology-of-everything/concept-skills)](https://skills.sh/ontology-of-everything/concept-skills)

> Name the meaning first — then write code, run a CLI, or draft a spec.

[concept-skills](https://github.com/ontology-of-everything/concept-skills) provides nine
capabilities as 18 localized [Agent Skills](https://agentskills.io/) for ontology, semantic layers,
and concept design. English uses the base name;
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

Current release is **2.0.0**. Existing `software-concept-architect-*` skills are explicit-only;
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
| [Software Concept Architect · Design](docs/skills/en/software-concept-architect-design.md) | 1.0.0 | development |
| [Software Concept Architect · PRD](docs/skills/en/software-concept-architect-prd.md) | 1.0.0 | development |
| [Software Concept Architect · Build](docs/skills/en/software-concept-architect-build.md) | 1.0.0 | development |
| [Software Concept Architect · Review](docs/skills/en/software-concept-architect-review.md) | 1.0.0 | development |
| [Software Concept Architect · Guardrails](docs/skills/en/software-concept-architect-guardrails.md) | 1.0.0 | development |
| [Software Concept Architect · Refine](docs/skills/en/software-concept-architect-refine.md) | 1.0.0 | development |

### Semantic Modeling

Model the business meaning of data, facts, dimensions, and relations.

| Skill | Version | ClawHub category |
| --- | --- | --- |
| [Data Knowledge Architect](docs/skills/en/data-knowledge-architect.md) | 1.1.0 | knowledge |

### Knowledge Management

Extract, connect, organize, and reuse knowledge from source material.

| Skill | Version | ClawHub category |
| --- | --- | --- |
| [Personal Knowledge Architect](docs/skills/en/personal-knowledge-architect.md) | 0.4.0 | knowledge |

### Learning Methods

Build and revise understanding around a learning goal and a key framework.

| Skill | Version | ClawHub category |
| --- | --- | --- |
| [Read It. Reframe It. Own It.](docs/skills/en/read-it-reframe-it-own-it.md) | 0.2.0 | knowledge |

<!-- skill-catalog:end -->

### Concept design workflow

Purpose-Driven Software Design. Based on Daniel Jackson’s concept design approach in _The Essence of Software_.

Names, display titles, and migration details: [Software Concept Architect](docs/software-concept-architect-migration.md).

Requirements to modules, with the concept model as the contract. Each skill stops at its own
boundary and hands off: `design` → `prd` / `build` → `review`.

Shared principle: synchronization may restrict behavior, never extend a concept contract. Check
contract conformance and purpose fulfillment separately.

Worked comparison: [Restaurant reserve](docs/examples/restaurant/en/README.md). One scenario, four
structures, and the complexity counts.

Per-skill details and taxonomy: [docs/catalog.yml](docs/catalog.yml).
Localization contract: [docs/localization.md](docs/localization.md).

## Install

Requires Node.js for `npx`.

Base names install English. Append `-cn` for Simplified Chinese.

ClawHub publishes only the English `skills/en` editions; Chinese editions remain on GitHub.

```bash
npx skills add ontology-of-everything/concept-skills \
  --skill <skill-name> \
  --agent cursor \
  --copy -y
```

`--agent` accepts `cursor`, `claude-code`, or `codex`. Several skills at once, and `--global` to
install into `~/.agents/skills/` (scanned by both Cursor and Codex) instead of the project's
`.agents/skills/`:

```bash
npx skills add ontology-of-everything/concept-skills \
  --skill software-concept-architect-design software-concept-architect-prd software-concept-architect-guardrails \
  --agent cursor codex \
  --global --copy -y
```

List what's available, or install from a local checkout while developing:

```bash
npx skills add ontology-of-everything/concept-skills --list
npx skills add ./skills/<skill-name> --skill <skill-name> --agent cursor --copy -y
```

Discovery: [skills.sh](https://skills.sh/ontology-of-everything/concept-skills) (groups in
[`skills.sh.json`](skills.sh.json)) · [SkillsMP](https://skillsmp.com/) (GitHub topics
`claude-skills`, `claude-code-skill`) · [ClawHub](https://clawhub.ai/).

Agent-specific notes: [Cursor](docs/agents/cursor.md) · [Claude Code](docs/agents/claude-code.md) ·
[Codex](docs/agents/codex.md).

Read a skill before using it — skills run with your agent's permissions.

## Usage

Skills normally activate from their description, so plain requests are enough. The
concept design workflow is explicit-only and must be named (`/software-concept-architect-design` in Cursor,
`$software-concept-architect-design` in Codex):

```text
$software-concept-architect-design model this requirement as independent concepts
$software-concept-architect-prd transcribe the confirmed model into a PRD
$software-concept-architect-guardrails drift src/orders
Turn this API into a semantic layer                 → data-knowledge-architect
```

To pin a skill explicitly: `/skill-name` in Cursor, `$skill-name` in Codex.

## Classic usage examples

Each skill has three requests from starter to intermediate; copy one row at a time. Install the skill first, attach
or select the requested source material, and replace example paths with real project paths.

### Read It. Reframe It. Own It

`read-it-reframe-it-own-it`

| Level | Example | Copyable request |
| --- | --- | --- |
| Starter | Understand one topic | `$read-it-reframe-it-own-it` Using the supplied excerpts on concept independence, build a short knowledge tree around my goal of deciding when two functions should be separate. Add one example to each branch. |
| Practical | Build a book knowledge tree | `$read-it-reframe-it-own-it` Using my supplied material from The Essence of Software, establish a framework for designing software with clear responsibilities and composable concepts. Organize the ideas, methods, and examples into a knowledge tree; distinguish source evidence from my inferences. |
| Intermediate | Turn the tree into a study sketchnote | `$read-it-reframe-it-own-it` Turn the confirmed The Essence of Software knowledge tree into a Chinese study sketchnote. Keep the central question, key branches, one application example, and review questions. Settle the image text first, then draw it with an available image-generation tool. |

The third example combines this knowledge-reframing skill with a separate image-generation
capability. [The English skill is on ClawHub](https://clawhub.ai/agenticweb4/skills/learning-read-it-reframe-it-own-it);
its marketplace URL uses a different slug from the repository installation name.

### Personal Knowledge Architect

`personal-knowledge-architect`

| Level | Example | Copyable request |
| --- | --- | --- |
| Starter | Extract methods from notes | `$personal-knowledge-architect` Extract scenarios, method concepts, and relevant entities from these five user-interview notes. Present a deduplicated skeleton with sources for my confirmation. |
| Practical | Build a reusable method library | `$personal-knowledge-architect` Organize these ten product-research notes and merge duplicate methods. After skeleton approval, fill in each method’s inputs, processing, outputs, and applicable scenarios; produce the three knowledge YAML files. |
| Intermediate | Connect knowledge across topics | `$personal-knowledge-architect` Organize these interview, requirements-analysis, and product-validation materials into reusable knowledge. Let the scenario “validate demand for a new product” invoke the extracted methods and tools; retain sources and validate references. |

### Data Knowledge Architect

`data-knowledge-architect`

| Level | Example | Copyable request |
| --- | --- | --- |
| Starter | Explain an order table | `$data-knowledge-architect` Use the supplied order-table DDL and field descriptions to identify business meanings, fact grain, and candidate dimensions and measures. Mark definitions without evidence as open decisions. |
| Practical | Align an API with its tables | `$data-knowledge-architect` Build a semantic model from the order OpenAPI contract and corresponding table schemas. Surface conflicting names, statuses, and metric definitions; emit OKF after decision-workbench approval. |
| Intermediate | Model orders, payments, and refunds | `$data-knowledge-architect` Build related semantic models for the supplied order, payment, and refund interfaces. Define their respective grains, shared dimensions, and measure semantics. Review cross-model decisions, then emit and validate OKF bundles after approval. |

### Software Concept Architect · Design

`software-concept-architect-design`

| Level | Example | Copyable request |
| --- | --- | --- |
| Starter | Design a task list | `$software-concept-architect-design` Design the concepts for a task list supporting adding, completing, and reopening tasks. Confirm user benefits and concept boundaries with me before specifying purpose, state, actions, and operational principle. |
| Practical | Design restaurant reservations | `$software-concept-architect-design` Design a restaurant system supporting reservations and cancellations. Establish the application purpose, concept responsibilities, and synchronization rules; evaluate the design against a complete reservation scenario. |
| Intermediate | Add a waiting list | `$software-concept-architect-design` Add waiting-list and vacancy-notification requirements to the confirmed reservation design. Compare extending existing concepts with introducing a new one; update affected models and synchronizations after confirmation. |

### Software Concept Architect · PRD

`software-concept-architect-prd`

| Level | Example | Copyable request |
| --- | --- | --- |
| Starter | Write a compact specification | `$software-concept-architect-prd` Transcribe the confirmed task-list concept model into a concise PRD, preserving purpose, state, actions, operational principle, and acceptance provenance. |
| Practical | Document the reservation system | `$software-concept-architect-prd` Transcribe the confirmed restaurant-reservation model into an overall PRD, per-concept CONCEPT.md files, and SYNCS.md. Trace acceptance criteria to purposes, scenarios, or behavioral contracts. |
| Intermediate | Update specifications incrementally | `$software-concept-architect-prd` Apply the confirmed waiting-list design to the affected PRD sections, concept specifications, synchronization rules, and acceptance criteria. Preserve existing human-written notes and mark open decisions. |

### Software Concept Architect · Build

`software-concept-architect-build`

| Level | Example | Copyable request |
| --- | --- | --- |
| Starter | Implement one independent concept | `$software-concept-architect-build` Implement the confirmed task-list concept in TypeScript as an in-memory module. Test adding, completing, and reopening tasks against its contract. |
| Practical | Implement reservations and cancellations | `$software-concept-architect-build` Implement a TypeScript backend from the confirmed reservation model and specifications. Keep concept modules independent, coordinate them through synchronization rules, and test reservation and cancellation scenarios. |
| Intermediate | Implement the waiting-list flow | `$software-concept-architect-build` Implement the confirmed waiting-list flow from cancellation through vacancy release to notification. Test the normal path and the failure cases defined in the specifications. |

### Software Concept Architect · Review

`software-concept-architect-review`

| Level | Example | Copyable request |
| --- | --- | --- |
| Starter | Review one concept design | `$software-concept-architect-review` Review this task-list concept model without editing it. Is its purpose clear, do its actions and operational principle support that purpose, and which conclusions lack evidence? |
| Practical | Check specification-to-code drift | `$software-concept-architect-review` Compare reservation requirements, concept specifications, and code. Check duplicate reservations, cancellations, and capacity release against the contracts; report concrete evidence and issue priorities. |
| Intermediate | Review the composed waiting-list behavior | `$software-concept-architect-review` Review the system after adding the waiting list. Check concept independence, contract-respecting synchronizations, end-to-end fitness for purpose, and effects on the existing reservation flow. |

### Software Concept Architect · Guardrails

`software-concept-architect-guardrails`

| Level | Example | Copyable request |
| --- | --- | --- |
| Starter | Audit specification coverage | `$software-concept-architect-guardrails` audit src/reservations Report missing concept specifications or synchronization documentation, with suggested follow-up commands. |
| Practical | Backfill a contract from code | `$software-concept-architect-guardrails` concept src/reservations Backfill CONCEPT.md from the existing code, distinguishing evidenced behavior, inferred purpose, and discovered design gaps. |
| Intermediate | Check drift across related modules | `$software-concept-architect-guardrails` drift src Compare the reservation and waiting-list modules against their CONCEPT.md and SYNCS.md files. Report drift evidence without automatically rewriting contracts. |

### Software Concept Architect · Refine

`software-concept-architect-refine`

| Level | Example | Copyable request |
| --- | --- | --- |
| Starter | Clarify one ambiguous concept | `$software-concept-architect-refine` Examine this Todo concept that manages task completion and reminder delivery. Use actual scenarios to assess overloading and recommend the smallest useful adjustment. |
| Practical | Decide whether similar concepts should merge | `$software-concept-architect-refine` Compare the purposes and behaviors of Favorites and Read Later. Assess whether to keep them separate, unify them, or specialize them; explain benefits and costs. |
| Intermediate | Refine an overloaded reservation module | `$software-concept-architect-refine` Inspect the Booking module that handles reservations, payments, notifications, and waiting lists. Use requirements, specifications, and code to locate overloading or synchronization problems and propose a minimal refactoring that preserves required behavior. |

**A connected workflow:** design and confirm the model → PRD → implementation → review. For an existing project, start with Guardrails audit, then backfill specifications or refine concepts as needed.

### Study sketchnote example

A Chinese study-note example for The Essence of Software: organize a knowledge tree around “How can I design clear, reusable software concepts?”, then turn it into a sketchnote.

![Chinese knowledge-tree sketchnote for The Essence of Software](docs/examples/reading/essence-of-software-study-notes.png)

This original example draws on Daniel Jackson’s [public
overview](https://essenceofsoftware.com/posts/distillation/) and [concept-criteria
tutorial](https://essenceofsoftware.com/tutorials/concept-basics/criteria/); the restaurant waiting-list flow is a
learner-created example. Generated with built-in imagegen, it is neither a reproduced book page nor a full-book
summary. [Image-generation prompt](docs/examples/reading/essence-of-software-study-notes.prompt.txt).

## Contributing

[docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) · [docs/authoring.md](docs/authoring.md)

```bash
./tools/skill-scaffold.sh <skill-name>   # new skill
./tools/install-git-hooks.sh             # pre-commit → validate-all.sh
./tools/validate-all.sh                  # all skills, same as CI
./qa/<skill-name>/validate.sh            # one skill
```

`skills/en/<name>/` and `skills/cn/<name>-cn/` are self-contained install payloads. QA follows the
same locale split and is never installed. Update both locales, catalog, docs, and parity checks
together.

## License

[Apache-2.0](LICENSE) © concept-skills contributors. Bundles published to
[ClawHub](https://clawhub.ai/) are MIT-0 there; the repository source stays Apache-2.0.
