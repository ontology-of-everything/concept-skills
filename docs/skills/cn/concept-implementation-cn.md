# 概念实现 · 模块单体

`concept-implementation-cn` · **Concept Implementation — Modular Monolith**

> 本文是给人看的中文说明，**不是** `npx skills add` 安装包内容。Agent 加载 [`skills/concept-implementation-cn/SKILL.md`](../../../skills/cn/concept-implementation-cn/SKILL.md)。

**Version:** 0.9.0 · Changelog:
[qa/concept-implementation-cn/CHANGELOG.md](../../../qa/cn/concept-implementation-cn/CHANGELOG.md)

## 一句话

仅显式调用 · 将确认模型实现为模块单体，保持概念独立与因果同步，规格共存，测试分别关联概念目的与应用目的

## 启用方式

本技能默认不自动启动。Cursor 用 `/concept-implementation-cn`，Codex 用 `$concept-implementation-cn`。

## 适用场景

- 概念模型已确认，需要代码结构而不是再讨论边界。
- 目标是模块单体，按动作与状态关系划分概念；端口-适配器按需采用。
- 语言细节按需加载：Rust、Java/Spring Modulith、TypeScript。

## 方法

1. 读模型、概念/应用目的与项目事实；模型缺陷回 design，转录错误回 prd，代码违约在本技能修复。
2. 概念模块互不引用；syncs 以具名规则承担业务协调；Requesting 或边缘适配器实现已确认入口策略。
3. mediator 或规则引擎保持因果、绑定及失败契约；需要响应时明确结果和请求关联。
4. 规格与代码共存；概念 OP、应用端到端场景及不变量分别验证，架构看护进入 CI。
5. 仅有工程痛点时分组/拆包；验证产品子集的目的、入口、剩余规则与构建支持。

## 安装载荷

```text
skills/concept-implementation-cn/
├── SKILL.md                     # 概念 / 约束 / 实现
├── agents/openai.yaml
└── references/
    ├── spec-format.md             # 共享规格契约与模板（独立安装副本）
    ├── scaling.md               # 概念分组与 syncs 拆包（十余个概念起）
    ├── rust.md
    ├── java-spring.md
    ├── typescript.md
    └── sources.md               # 取用原则的出处
```

```bash
npx skills add ontology-of-everything/concept-skills \
  --skill concept-implementation-cn \
  --agent cursor \
  --copy -y
```

Local checkout:

```bash
npx skills add ./skills/concept-implementation-cn \
  --skill concept-implementation-cn \
  --agent cursor \
  --copy -y
```

## Marketplaces

- [skills.sh](https://skills.sh/ontology-of-everything/concept-skills/concept-implementation-cn)
- [SkillsMP](https://skillsmp.com/) — repo topics `claude-skills`, `claude-code-skill`
- [ClawHub](https://clawhub.ai/agenticweb4/concept-implementation-cn)

## 2026-09-25 修订

同步规则自身保持模块化；组合层指导合入 SKILL.md。按 Jackson 2026 年论文区分动作、查询与请求，明确工程实现选择。

## 2026-09-07 修订

修复事务/错误处理、完成事件与并发隔离；纠正 Spring Modulith 与 Cargo 边界检查说明。

依据与检索边界见[研究记录](../references/jackson/2026-09-07-concept-research.md)。

## 2026-09-13 修订

关联概念 OP 与应用端到端验证；区分组合根装配、业务协调与根因修复路由。

## 2026-09-14 修订

实现契约明确抽象状态读取、case 判别、同 flow 对象关联及旧接口映射。

[统一规格与模板](../../../skills/cn/concept-implementation-cn/references/spec-format.md) 以 WYSIWID v1 §4–6 为基线，区分论文语义、本地扩展与旧格式兼容。

## 2026-09-19 修订

同步可收窄行为，不可扩展概念契约；逐概念核对组合中的动作、状态变化与输出序列，并另查目的是否落空。精简重复定义与指导。
