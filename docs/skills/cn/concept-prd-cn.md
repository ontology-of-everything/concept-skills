# 概念 PRD

`concept-prd-cn` · **Concept PRD**

> 本文是给人看的中文说明，**不是** `npx skills add` 安装包内容。Agent 加载 [`skills/concept-prd-cn/SKILL.md`](../../../skills/cn/concept-prd-cn/SKILL.md)。

**Version:** 0.7.1 · Changelog:
[qa/concept-prd-cn/CHANGELOG.md](../../../qa/cn/concept-prd-cn/CHANGELOG.md)

## 一句话

仅显式调用 · 将确认模型转录为总体 PRD、概念规格与同步规则，保留概念/应用目的、论证前提、未决取舍及验收追溯

## 启用方式

本技能默认不自动启动。Cursor 用 `/concept-prd-cn`，Codex 用 `$concept-prd-cn`。

## 适用场景

- 概念模型已确认，需要可导航、可验收的规格文档。
- 后续要按概念独立验证，或按 flow 看出欠同步与过同步。
- 发现模型缺口时应回到 `concept-design`，而不是在文档里填补。

## 方法

1. 核对已确认模型及现有落点，总体 PRD 保存应用目的、场景、概念索引、图与未决。
2. 每概念一份 CONCEPT，四节不依赖其他概念定义，同名局部类型参数合法；保留概念目的与 OP 前提。
3. SYNCS 转录期单文件，按 flow 职责组织；实现拆包后规格随包迁移，索引保持唯一。
4. 验收分别追溯到概念 OP、应用场景及行为契约；缺口不补造，不写实现。

## 安装载荷

```text
skills/concept-prd-cn/
├── SKILL.md                 # 焦点 / 定义与关系 / 执行 / 完成条件 / 参考
├── agents/openai.yaml
└── references/
    ├── spec-format.md             # 共享规格契约与模板（独立安装副本）
    ├── templates.md         # CONCEPT.md / SYNCS.md 文件编排
    ├── example-reserving.md # 填好的餐厅订位例（转录后的文件形态）
    └── sources.md           # 取用原则的出处
```

```bash
npx skills add ontology-of-everything/concept-skills \
  --skill concept-prd-cn \
  --agent cursor \
  --copy -y
```

Local checkout:

```bash
npx skills add ./skills/concept-prd-cn \
  --skill concept-prd-cn \
  --agent cursor \
  --copy -y
```

## Marketplaces

- [skills.sh](https://skills.sh/ontology-of-everything/concept-skills/concept-prd-cn)
- [SkillsMP](https://skillsmp.com/) — repo topics `claude-skills`, `claude-code-skill`
- [ClawHub](https://clawhub.ai/agenticweb4/concept-prd-cn)

## 2026-09-07 修订

明确权威规格与增量编辑；修复验收追溯、错误查询和文件格式；压缩重复示例。

依据与检索边界见[研究记录](../references/jackson/2026-09-07-concept-research.md)。

## 2026-09-13 修订

保留概念与应用两层目的、论证前提和验收追溯；未决内容不由模板补造。

## 2026-09-14 修订

按共享格式转录概念和 sync；文件编排与语法分离，订位例保留分支、绑定及未决。

[统一规格与模板](../../../skills/cn/concept-prd-cn/references/spec-format.md) 以 WYSIWID v1 §4–6 为基线，区分论文语义、本地扩展与旧格式兼容。

## 2026-09-19 修订

同步可收窄行为，不可扩展概念契约；逐概念核对组合中的动作、状态变化与输出序列，并另查目的是否落空。精简重复定义与指导。
