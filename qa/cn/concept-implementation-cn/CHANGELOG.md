# concept-implementation-cn Changelog

## 0.9.0 - 2026-09-25

- 明确同步规则可独立定位与验证；依据 Jackson 最新论文区分动作、查询、请求和完成事件。
- 将组合层指导合入技能入口，厘清模块布局及可靠性措施中的本仓工程选择。

## 0.8.1 - 2026-09-19

- 明确同步可收窄行为、不可扩展契约；以逐概念行为序列核对组合，区分合法限制与目的落空。
- 精简技能入口的重复定义与检查说明，保持共享规格和中英文一致。

## 0.8.0 - 2026-09-14

- 实现契约明确抽象状态读取、case 判别、同 flow 对象关联及旧接口映射。
- 共享规格按单一源分发，各独立安装包由校验门禁检查副本一致性。

## 0.7.0 - 2026-09-13

- 关联概念 OP 与应用端到端验证；区分组合根装配、业务协调与根因修复路由。
- 统一概念族术语与职责，精简重复指导；同步文档和行为评估。

## 0.6.0 - 2026-09-10

### Changed

- Default off: run only on explicit `$concept-implementation-cn` /
  `/concept-implementation-cn`. Codex `allow_implicit_invocation: false`.
- `references/scaling.md`: `wyx:map` → `concept-guardrails map` (guardrails 0.30.0
  dropped the `wyx:` prefix).

## 0.5.0 - 2026-09-07

- 修复事务/错误处理、完成事件与并发隔离；纠正 Spring Modulith 与 Cargo 边界检查说明。
- 核验最新相关论文，更新行为评估及文档。

Skill-only history. Repository tooling changes: [../../CHANGELOG.md](../../CHANGELOG.md).

## 0.4.0 - 2026-09-07

### Changed

- Rename the installable skill from `jackson-concept-implementation-cn` to
  `concept-implementation-cn` (concept-* family prefix); companion references
  updated
- Restructure SKILL.md into the six-section skeleton (目标 / 原则 / 流程 /
  命题 / 记法与模板 / 参考) and cut it to ~48% of its size (10.3 KB → 5.0 KB).
  Sync landing routes, timing/error isolation, syncs-layer discipline,
  interface layer, failure paths, and spec colocation move to
  `references/composition-layer.md`; concept grouping and sync packaging
  to `references/scaling.md`; sources to `references/sources.md`. The
  mapping table stays inline; no rules were dropped

## 0.3.0 - 2026-08-28

### Added

- Scaling section: concept grouping (a.k.a. domain folders) as pure code
  organization with zero architectural semantics — the zero-reference rule
  stays flat across all concepts (no intra-group references, no "group
  interfaces", no new guard rules); directory-only by default, build
  boundaries as an optional upgrade
- Groups derive from the extrinsic dependency graph plus flow affinity,
  team ownership as tie-breaker; groups double as shippable product subsets
- Syncs-layer split: flow modules regroup into per-group sync packages
  (flows never split); cross-group flows land in the group owning the entry
  Requesting action; each sync package carries its own SYNCS.md with a
  local coordination graph (global view = overall PRD graph + wyx:map)
- New violation signal: citing same-group membership to reference a sibling
  concept, or inventing "group interfaces"
- Language references gain nested grouping layouts (cargo glob members,
  Spring Modulith nested application modules, pnpm workspace globs)

## 0.2.0 - 2026-08-28

### Changed

- Sync semantics updated to the author's current causal-rule model
  (when/where/then, Requesting pseudo-concept): transactions are an optional
  single-DB reinforcement, error syncs are the default failure path
- Add implementation-layer timing/error-isolation classification
  (post-action / pre-validation / scheduled), adapted from wyx, explicitly
  marked as engineering taxonomy that does not change design semantics
- Map underscore-prefixed queries to read-only module methods; add a spec
  colocation step (CONCEPT.md into module dirs, SYNCS.md into the syncs dir)
  enabling wyx drift detection and spec-first edits

## 0.1.0 - 2026-08-28

### Added

- Initial Jackson concept-implementation-cn skill: map a confirmed concept model
  onto a modular monolith (one module per concept, syncs as mediators, the
  dependency graph as build/cut order)
- Two official sync landings: procedural mediator (default) and a declarative
  rule engine; concept modules stay mutually unreferenced
- Language notes for Rust, Java/Spring Modulith, and TypeScript, loaded only
  for the target language
