# concept-skills

[![skills.sh](https://skills.sh/b/ontology-of-everything/concept-skills)](https://skills.sh/ontology-of-everything/concept-skills)

> Name the meaning first — then write code, run a CLI, or draft a spec.

[concept-skills](https://github.com/ontology-of-everything/concept-skills) provides seven
capabilities as 14 localized [Agent Skills](https://agentskills.io/) for ontology, semantic layers,
and concept design. English uses the base name;
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

Current release is **1.2.0**. The `concept-*` family is explicit-only; `concept-guardrails` modes
consume Jackson notation only.

## Table of Contents

- [Skills](#skills)
- [Install](#install)
- [Usage](#usage)
- [Contributing](#contributing)
- [Changelog](CHANGELOG.md)
- [License](#license)

## Skills

### Concept design

Requirements to modules, with the concept model as the contract. Each skill stops at its own
boundary and hands off: `design` → `prd` / `implementation` → `audit`.

Shared principle: synchronization may restrict behavior, never extend a concept contract. Check
contract conformance and purpose fulfillment separately.

Worked comparison: [Restaurant reserve](docs/examples/restaurant/en/README.md). One scenario, four
structures, and the complexity counts.

| English                                                              | 中文                                                                       | What it does                                                                |
| -------------------------------------------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| [`concept-design`](docs/skills/en/concept-design.md)                 | [`concept-design-cn`](docs/skills/cn/concept-design-cn.md)                 | Designs independent concepts and synchronizations.                          |
| [`concept-prd`](docs/skills/en/concept-prd.md)                       | [`concept-prd-cn`](docs/skills/cn/concept-prd-cn.md)                       | Transcribes confirmed models into traceable PRDs and specifications.        |
| [`concept-implementation`](docs/skills/en/concept-implementation.md) | [`concept-implementation-cn`](docs/skills/cn/concept-implementation-cn.md) | Implements independent modules and synchronization composition.             |
| [`concept-audit`](docs/skills/en/concept-audit.md)                   | [`concept-audit-cn`](docs/skills/cn/concept-audit-cn.md)                   | Audits design arguments, drift, composition, and optional code conformance. |
| [`concept-guardrails`](docs/skills/en/concept-guardrails.md)         | [`concept-guardrails-cn`](docs/skills/cn/concept-guardrails-cn.md)         | Creates, audits, compares, and maps colocated specifications.               |

### Ontology and semantics

Enterprise knowledge from APIs and databases (`semantic-km-creator`); personal knowledge from source
text (`semantic-pkm-creator`).

| English                                                          | 中文                                                                   | What it does                                                  |
| ---------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------- |
| [`semantic-km-creator`](docs/skills/en/semantic-km-creator.md)   | [`semantic-km-creator-cn`](docs/skills/cn/semantic-km-creator-cn.md)   | Builds evidence-only Kimball semantic layers from interfaces. |
| [`semantic-pkm-creator`](docs/skills/en/semantic-pkm-creator.md) | [`semantic-pkm-creator-cn`](docs/skills/cn/semantic-pkm-creator-cn.md) | Extracts scenes, concepts, and entities from source text.     |

Per-skill details: `docs/skills/en/` and `docs/skills/cn/`. Machine-readable index:
[docs/catalog.yml](docs/catalog.yml). Localization contract:
[docs/localization.md](docs/localization.md).

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
  --skill concept-design concept-prd concept-guardrails \
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

Skills normally activate from their description, so plain requests are enough. The `concept-*`
family is explicit-only and must be named (`/concept-design` in Cursor, `$concept-design` in Codex):

```text
$concept-design model this requirement as independent concepts
$concept-prd transcribe the confirmed model into a PRD
$concept-guardrails audit specification drift in src/orders
Turn this API into a semantic layer                 → semantic-km-creator
```

To pin a skill explicitly: `/skill-name` in Cursor, `$skill-name` in Codex.

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
