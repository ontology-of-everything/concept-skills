# concept-audit Changelog

## 0.7.1 - 2026-09-19

- Make synchronization restriction explicit: each composed concept trace must satisfy its own contract; distinguish restriction from purpose failure.
- Condense repeated entrypoint definitions and checks; keep shared contracts and locales aligned.

## 0.7.0 - 2026-09-14

- 审计共享规格契约，补查空输出误判成功、对象错配、状态基数与分支漂移。
- 共享规格按单一源分发，各独立安装包由校验门禁检查副本一致性。

## 0.6.0 - 2026-09-13

- 支持无代码的设计审查；区分概念论证、应用组合适切性与实现符合性，按证据路由修复。
- 统一概念族术语与职责，精简重复指导；同步文档和行为评估。

## 0.5.0 - 2026-09-10

### Changed

- Default off: run only on explicit `$concept-audit` / `/concept-audit`. Codex
  `allow_implicit_invocation: false`.

## 0.4.0 - 2026-09-07

- 审计按行为与影响判定；补充绑定/合取/重放检查，消除合法循环、日志与组织方式误报。
- 核验最新相关论文，更新行为评估及文档。

Skill-only history. Repository tooling changes: [../../CHANGELOG.md](../../CHANGELOG.md).

## 0.3.0 - 2026-09-07

### Changed

- Rename the installable skill from `jackson-concept-audit` to
  `concept-audit` (concept-* family prefix); companion references updated.
 ; content is unchanged

## 0.2.0 - 2026-08-28

### Changed

- Spec-drift dimension operationalized with calibrated checklists adapted
  from jlifyio/wyx: per-CONCEPT.md and per-SYNCS.md check categories with
  fixed severities, cross-spec reference validation, and systemic-pattern
  aggregation
- Severity calibration rules: spec silence is not drift, verbatim severities
  with reclassification instead of in-category upgrades, Low dedup, and
  verify-in-current-code before reporting Medium+
- Parallel scan for 5+ specs via read-only subagents pinned to a strong
  model, each covering 2-3 adjacent specs with per-category verdicts
- Spec discovery now covers colocated CONCEPT.md/SYNCS.md plus docs/prd/;
  new check for spec naming violations (cross-concept names or
  interactions/dependencies sections inside concept specs)

## 0.1.0 - 2026-08-28

### Added

- Initial Jackson concept-audit skill: read-only five-dimension check of an
  existing codebase against its concept model or PRD family
- Dimensions: spec drift, boundary violations, criteria review, composition
  quality, and dependency/subset integrity, each with a single fix-routing
  target
- Findings require location and evidence; repair order is upstream-first
  (design → prd → implementation)
