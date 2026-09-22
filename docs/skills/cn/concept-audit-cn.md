# 概念审计

`concept-audit-cn` · **Concept Audit**

> 本文是给人看的中文说明，**不是** `npx skills add` 安装包内容。Agent 加载 [`skills/concept-audit-cn/SKILL.md`](../../../skills/cn/concept-audit-cn/SKILL.md)。

**Version:** 0.7.1 · Changelog:
[qa/concept-audit-cn/CHANGELOG.md](../../../qa/cn/concept-audit-cn/CHANGELOG.md)

## 一句话

仅显式调用 · 只读审查概念与应用目的兑现论证；有代码时再核对实现符合性，覆盖适切性、独立性、组合、漂移和产品子集，按证据与根因路由修复

## 启用方式

本技能默认不自动启动。Cursor 用 `/concept-audit-cn`，Codex 用 `$concept-audit-cn`。

## 适用场景

- 尚无代码的概念/应用设计需要审查，或已有模型需核对代码符合性。
- 模块互引、共享表、DTO 进概念签名等边界问题需要定位，而不是立刻改代码。
- 持续看护已由 CI 架构测试承担，需要一次周期或按需的人工审计。

## 方法

1. 读取需求、概念与应用模型；有代码时再沿入口读取实现、状态和测试。
2. 分别审查概念契约 → OP → 概念目的，以及概念选择/同步 → 应用场景 → 应用目的。
3. 检查独立性、组合、漂移与产品子集；缺失材料标未核实，不把无代码误报成实现缺陷。
4. 按当前证据、实际影响及根因聚合发现，路由到 design / prd / implementation。
5. 全程只读，不修改规格、代码或历史。

## 安装载荷

```text
skills/concept-audit-cn/
├── SKILL.md                         # 焦点 / 定义与关系 / 执行 / 完成条件 / 参考
├── agents/openai.yaml
└── references/
    ├── spec-format.md             # 共享规格契约与模板（独立安装副本）
    ├── drift-checklist.md           # 漂移检查表、严重度校准、并行扫描
    ├── composition-checklist.md     # 组合缺陷检查表
    └── sources.md                   # 取用原则的出处
```

```bash
npx skills add ontology-of-everything/concept-skills \
  --skill concept-audit-cn \
  --agent cursor \
  --copy -y
```

Local checkout:

```bash
npx skills add ./skills/concept-audit-cn \
  --skill concept-audit-cn \
  --agent cursor \
  --copy -y
```

## Marketplaces

- [skills.sh](https://skills.sh/ontology-of-everything/concept-skills/concept-audit-cn)
- [SkillsMP](https://skillsmp.com/) — repo topics `claude-skills`, `claude-code-skill`
- [ClawHub](https://clawhub.ai/agenticweb4/concept-audit-cn)

## 2026-09-07 修订

审计按行为与影响判定；补充绑定/合取/重放检查，消除合法循环、日志与组织方式误报。

依据与检索边界见[研究记录](../references/jackson/2026-09-07-concept-research.md)。

## 2026-09-13 修订

支持无代码的设计审查；区分概念论证、应用组合适切性与实现符合性，按证据路由修复。

## 2026-09-14 修订

审计共享规格契约，补查空输出误判成功、对象错配、状态基数与分支漂移。

[统一规格与模板](../../../skills/cn/concept-audit-cn/references/spec-format.md) 以 WYSIWID v1 §4–6 为基线，区分论文语义、本地扩展与旧格式兼容。

## 2026-09-19 修订

同步可收窄行为，不可扩展概念契约；逐概念核对组合中的动作、状态变化与输出序列，并另查目的是否落空。精简重复定义与指导。
