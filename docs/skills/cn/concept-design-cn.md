# 概念设计

`concept-design-cn` · **Concept Design**

> 本文是给人看的中文说明，**不是** `npx skills add` 安装包内容。Agent 加载 [`skills/concept-design-cn/SKILL.md`](../../../skills/cn/concept-design-cn/SKILL.md)。

**Version:** 0.8.2 · Changelog:
[qa/concept-design-cn/CHANGELOG.md](../../../qa/cn/concept-design-cn/CHANGELOG.md)

## 一句话

仅显式调用 · 和用户一起完成概念设计；先确认对齐，再写设计记录

## 启用方式

本技能默认不自动启动。Cursor 用 `/concept-design-cn`，Codex 用 `$concept-design-cn`。

## 适用场景

- 需求还停留在功能、页面或实体清单，需要找到用户真正要掌握的功能单元。
- 已有概念模型出现边界糊模、功能碎片、交叉依赖或命名陌生。
- 需要在进入 PRD、架构或代码前，先确认用户面向的心理模型和行为边界。

## 方法

1. 明确应用目的、受益者、现状与约束；既有系统追踪实际入口、状态及失败路径。
2. 定义各概念的 purpose、OP、state/actions，区分概念目的与整体应用目的。
3. 审查契约是否支持 OP、OP 是否兑现概念目的；用事实和反例修正边界。
4. 选择并同步概念，以端到端场景检查应用目的；组合保持概念行为，分别画同步图与产品依赖图。
5. 和用户确认对齐三节后写入设计记录；待确认项留在排除与未决，按授权继续文档或实现。

## 安装载荷

```text
skills/concept-design-cn/
├── SKILL.md                       # 原则 / 流程 / 产物索引 / 标准索引 / 完成标准
├── agents/openai.yaml
└── references/
    ├── artifacts.md               # 对齐三节与设计记录的字段
    ├── spec-format.md             # 共享规格契约与模板（独立安装副本）
    ├── criteria.md                # 概念定义与八项资格的决策依据
    ├── sync-notation.md           # 应用场景、sync 语义、图与产品依赖
    ├── example-reserving.md       # 填好的 Beyond Objects 餐厅订位例
    └── sources.md                 # 作者原文与取用原则
```

```bash
npx skills add ontology-of-everything/concept-skills \
  --skill concept-design-cn \
  --agent cursor \
  --copy -y
```

Local checkout:

```bash
npx skills add ./skills/concept-design-cn \
  --skill concept-design-cn \
  --agent cursor \
  --copy -y
```

## Marketplaces

- [skills.sh](https://skills.sh/ontology-of-everything/concept-skills/concept-design-cn)
- [SkillsMP](https://skillsmp.com/) — repo topics `claude-skills`, `claude-code-skill`
- [ClawHub](https://clawhub.ai/agenticweb4/concept-design-cn)

## 2026-09-07 修订

区分论文语义与本仓方言；修复 flow、绑定、查询空集与同步图；压缩模板并重写订位教学例。

依据与检索边界见[研究记录](../references/jackson/2026-09-07-concept-research.md)。

## 2026-09-13 修订

以定义和关系组织建模知识；分别论证概念目的与应用目的，补充基于事实的反例检查。

## 2026-09-14 修订

统一概念与 sync 规格契约，明确具名签名、状态关系、输出分支与旧方言迁移；精简入口和重复模板。

[统一规格与模板](../../../skills/cn/concept-design-cn/references/spec-format.md) 以 WYSIWID v1 §4–6 为基线，区分论文语义、本地扩展与旧格式兼容。

## 2026-09-19 修订

同步可收窄行为，不可扩展概念契约；逐概念核对组合中的动作、状态变化与输出序列，并另查目的是否落空。精简重复定义与指导。
