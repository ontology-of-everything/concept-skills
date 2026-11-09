# concept-skills

Concept design, semantic modeling, knowledge organization and visual teaching.

## Repository ownership

| Repository | Owns |
| --- | --- |
| `concept-skills` | Software concepts, semantic modeling, knowledge organization, and visual learning. |
| `cloud-concept-skills` | Huawei Cloud operations, billing, controlled provisioning, and account onboarding. |
| `myoffice-skills` | Office workflows, presentations, source notes, repository guidance, and Agent DX tooling. |

## Directory contract

| Directory | Contract |
| --- | --- |
| `skills/en/<name>/`, `skills/zh-CN/<name>-cn/` | Self-contained install payloads, including required `references/`, assets and scripts. |
| `qa/` | Private local validation, fixtures and reports; ignored by Git and absent from public checkouts. |
| `catalog.yml` | Tracked discovery metadata used by QA and publishing tools. |
| `docs/` | Concise local notes and examples; ignored by Git and never required by QA or distribution. |
| `tools/`, `.githooks/`, `.github/` | Repository tooling, local commit/push gates and CI. |

Learning copies, downloaded repositories, process notes, raw outputs and generated eval workspaces
belong outside the checkout, normally in a task-specific temporary directory. Delete them when no
longer needed. Preserve packaged `skills/**/references/` and maintained fixtures/examples.

## Change and release rules

- Update the owning repository; keep sibling projects independent and link rather than copy their skills.
- Keep localized pairs, declared source versions and `catalog.yml` consistent; the catalog is the public version record. English uses the base
  name and `language: en`; Chinese adds `-cn` and `language: zh-CN`. Paired `translation_of` values
  name each other. Translate prose while preserving commands, safety gates and observable behavior.
  The repository `VERSION` and per-skill catalog versions have separate scopes.
- Run `./tools/validate-all.sh` for public package checks; it must work without `qa/`.
  Run `./tools/validate-all.sh --local-qa` only for available local QA; no behavioral or live-service result is implied by public checks.
- Set `git config core.hooksPath .githooks` once per checkout. Ignore rules and commit/push/CI hygiene checks
  keep local-only files out of Git, including files added with force.
- Commit and publish only within user authorization. ClawHub publishes the editions enabled in
  `catalog.yml`; Chinese skill IDs retain `-cn`. Verify remote contents before announcing a release.
- Treat credentials, local installs and caches as local-only. Keep only the current release notes;
  rewriting Git history or deleting remote releases requires explicit user authorization.
- Keep `qa/`, `docs/`, analysis material and generated reports local; exclude them even when force-added.

## Skill authoring structure

Organize each SKILL.md around its scope, inputs, steps, and completion checks. Add a heading only when it separates useful content. Keep definitions and specification syntax in the shared contract; load task-specific references as needed. Keep each sentence to one point. Use the same term for the same concept. Use RFC 2119 keywords for testable obligations, not general advice. Keep the concept entry and the other three capabilities compact.

## Domain language

Use these terms consistently in both locales. Preserve syntax, file names, quoted source text, and external standard names.

| Term | Chinese | Meaning |
| --- | --- | --- |
| model | 模型 | The design's concepts, behavior, and composition. |
| specification | 规格 | The written expression of a model. |
| contract | 契约 | Allowed behavior that an implementation must preserve. |
| specification conventions | 规格约定 | This repository's notation and interpretation rules in spec-format.md. |
| concept | 概念 | An independent software behavior with its own purpose, state, and actions. |
| concept instance | 概念实例 | A particular instance that owns its state. |
| operational principle, OP | 运作原理，OP | A representative history that explains how a concept fulfills its purpose. |
| composition | 组合 | Application-specific coordination outside concepts, organized into cohesive rule groups. |
| synchronization rule | 同步规则 | External coordination of concept actions. Code may use a `<BusinessEffect>Mediator` name. |
| port, adapter | 端口、适配器 | An inner contract for needed interaction, and its technical implementation. |
| facade | 门面 | An optional stable application entry; coordination remains in named rules. |
| action invocation | 动作调用 | A request to execute an action. |
| action completion | 动作完成记录 | A declared result of an executed action. |
| action occurrence | 动作发生记录 | An identified execution that connects invocation and completion. |
| runtime flow | 运行时 flow | A root event and its causal descendants. |
| query | 查询 | A read that returns binding rows without an action completion. |
| grain | 粒度 | What one fact record represents. |
| fact, dimension, measure, metric | 事实、维度、度量、指标 | Analytical terms defined by the data skill. They are not Jackson concept categories. |

The personal-knowledge skill uses concept for a reusable method and states that local meaning explicitly. Do not apply one skill family's qualification criteria to a different family. Keep confirmed, proposed, inferred, and unresolved statements distinct. Reuse existing confirmation when its scope and content still apply.

## Concept-specific rules

- `catalog.yml` is the discovery source of truth. After catalog changes, run
  `python3 tools/skill-catalog.py --write`; the validation gate checks generated README sections and `skills.sh.json`.
- Concept Design has one entry per language: `concept-design` and `concept-design-cn`. The former eight workflows
  are combined here; the other seven entries are retired, not aliases. The other three capability families remain separate.
- Maintain core definitions and principles in `concept-design/SKILL.md`; keep specification conventions in
  `references/shared/model/spec-format.md`. Link directly to each `references/modes/<mode>/workflow.md`.
  Keep mode-specific references beside their workflow and cross-mode references in `references/shared/`.
  There are no shared skill dependencies or generated cross-package copies.
- The modes are prompt selectors, not shell commands. `scripts/concept_lint.py` is the actual read-only
  concept-lint CLI. It checks local specification structure, when/then records, and rule-name uniqueness
  across supplied files for one app. Unknown/legacy call notation returns `not_checked`/exit 3; only `format_checked` exits 0.
  Never report syntax checks as semantic proof.
- Keep decision-record status values and format examples consistent with the checker. Public checks
  run packaged examples and representative failing inputs.
- `guard map` generates the local Concept and Synchronization Diagram, not Jackson's purpose-dependence diagram.
  Keep `references/shared/artifacts/map-format.md` and `scripts/concept_map.py` aligned. Version 1 emits one Markdown document;
  it shares lexical handling with concept-lint and never fills unknown references by inference.
- Diagrams use Mermaid in Markdown. Keep explanation views concise and use the map generator for concept/synchronization diagrams.
- Author locale packages directly under `skills/` and register them in `catalog.yml`; keep QA and generated artifacts local.
