# concept-design Changelog

## 0.8.2 - 2026-09-22

- Complete the concept design with the user: confirm the alignment, then write the design record.
- State the concept definition and the decision basis for each of the eight criteria, including
  distinctions for classes, features, user stories, and microservices.
- Condense repeated wording, and name intrinsic/extrinsic dependencies, tighten/loosen, and the
  three design-move pairs.

## 0.8.1 - 2026-09-19

- Make synchronization restriction explicit: each composed concept trace must satisfy its own contract; distinguish restriction from purpose failure.
- Condense repeated entrypoint definitions and checks; keep shared contracts and locales aligned.

## 0.8.0 - 2026-09-14

- 统一概念与 sync 规格契约，明确具名签名、状态关系、输出分支与旧方言迁移；精简入口和重复模板。
- 共享规格按单一源分发，各独立安装包由校验门禁检查副本一致性。

## 0.7.0 - 2026-09-13

- 以定义和关系组织建模知识；分别论证概念目的与应用目的，补充基于事实的反例检查。
- 统一概念族术语与职责，精简重复指导；同步文档和行为评估。

## 0.6.0 - 2026-09-10

### Changed

- Default off: run only on explicit `$concept-design` / `/concept-design`.
  Codex `allow_implicit_invocation: false`.

## 0.5.0 - 2026-09-07

- 区分论文语义与本仓方言；修复 flow、绑定、查询空集与同步图；压缩模板并重写订位教学例。
- 核验最新相关论文，更新行为评估及文档。

Skill-only history. Repository tooling changes: [../../CHANGELOG.md](../../CHANGELOG.md).

## 0.4.1 - 2026-09-07

### Added

- `references/example-reserving.md`: filled Beyond Objects restaurant
  example (Reserving [User, Slot], Availability [Venue], when/where/then)

## 0.4.0 - 2026-09-07

### Changed

- Rename the installable skill from `jackson-concept-design` to
  `concept-design`; the concept-* family now shares one prefix with
  `concept-prd`, `concept-implementation`, `concept-audit`, and
  `concept-guardrails`
- Restructure SKILL.md into the six-section skeleton (目标 / 原则 / 流程 /
  命题 / 记法与模板 / 参考) and cut it to ~46% of its size (14.0 KB → 6.5 KB).
  The design loop now routes to on-demand references: criteria and
  misjudgment table → `references/criteria.md`; sync notation, causal
  semantics, signals, dependency graph → `references/sync-notation.md`;
  source list with one extracted principle per source →
  `references/sources.md`. Completion conditions become checkable
  propositions; no rules were dropped
- Make sync design explicit: principles now state sync as the sole
  composition mechanism (behavior preservation, Requesting entry, errors as
  matchable outputs) and that composition has structure — syncs grouped by
  flow, plus two deliverables: a coordination graph (who triggers whom) and
  the dependency graph (who cannot ship without whom). Flow step 5 is broken
  into sub-steps; the output template gains a `## 同步图` section and a
  flow-grouped sync block with an error sync; `references/sync-notation.md`
  gains a "结构：flow 与同步图" section (cascade rules, decomposition signals)

## 0.3.0 - 2026-08-28

### Changed

- Adopt the author's current notation (Beyond Objects, 2026): syncs move to
  when/where/then causal-rule semantics with the Requesting pseudo-concept;
  the book's CSP/transactional sync semantics is marked deprecated by the
  author himself
- Structured concept spec format: Alloy-style relational state, action
  signatures with requires/ensures and error output cases, underscore-prefixed
  read-only queries, after/then operational principles
- Concept specs stay zero-naming (no interactions/dependencies sections);
  an optional notes section is the only sanctioned place for context-of-use
  remarks (per the 6.1040 concept rubric); output format is wyx-compatible

## 0.2.0 - 2026-08-28

### Changed

- Expand Sync guidance with include/sync notation, reactive/atomic/behavior-
  preserving semantics, and undersync, oversync, flow, and synergy signals
- Expand the dependency graph into Parnas uses-relation subsets for MVP and
  teaching/build order
- After model confirmation, route documentation to `jackson-concept-prd`,
  code to `jackson-concept-implementation`, and existing-code review to
  `jackson-concept-audit`

## 0.1.0 - 2026-08-27

### Added

- Initial Jackson concept-design skill for turning requirements into concepts
  defined by purpose, operational principle, state, and actions
- Boundary critique using specificity, completeness, independence, and
  familiarity, with application behavior composed through synchronizations
- Explicit stop at model confirmation, before PRD, architecture, or code
