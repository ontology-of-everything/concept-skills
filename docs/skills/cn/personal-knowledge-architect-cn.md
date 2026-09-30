# 个人知识架构师 — 把原文组织成相互关联、可复用的知识

`personal-knowledge-architect-cn` · **个人知识架构师 — 把原文组织成相互关联、可复用的知识**

> 本文是给人看的中文说明，**不是** `npx skills add` 安装包内容。Agent 加载 [`skills/cn/personal-knowledge-architect-cn/SKILL.md`](../../../skills/cn/personal-knowledge-architect-cn/SKILL.md)。
>
> 面向**个人知识库**。企业接口 / 数据库走 [`data-knowledge-architect`](../en/data-knowledge-architect.md)。

**Version:** 0.4.0 · Changelog:
[qa/cn/personal-knowledge-architect-cn/CHANGELOG.md](../../../qa/cn/personal-knowledge-architect-cn/CHANGELOG.md)

## 一句话

按两轮流程把线性原文萃成可调用的场景、概念与实体：先扫骨架等人确认，再回查原文填 IPO、分解、组装与关系。

三层划分灵感来自「人月聊 IT」《三层架构：场景、概念与实体》。

## 三层

| 层 | 角色 |
| --- | --- |
| 概念 | 中枢：可执行动作；IPO 或分解 |
| 实体 | 可指认实例：人 / 工具 / 产品 / 具名框架 |
| 场景 | 组装：问题 + 编排规则，只调用已成立的概念与实体 |

## 安装载荷

```text
skills/cn/personal-knowledge-architect-cn/
├── SKILL.md                    # 目标 / 原则 / 流程 / 命题 / 记法与模板 / 参考
└── references/
    └── relations.md            # 八种关系与判定顺序
```

```bash
npx skills add ontology-of-everything/concept-skills \
  --skill personal-knowledge-architect-cn \
  --agent cursor \
  --copy -y
```

Local checkout:

```bash
npx skills add ./skills/cn/personal-knowledge-architect-cn \
  --skill personal-knowledge-architect-cn \
  --agent cursor \
  --copy -y
```

## Marketplaces

- [skills.sh](https://skills.sh/ontology-of-everything/concept-skills/cn/personal-knowledge-architect-cn)
- [SkillsMP](https://skillsmp.com/) — repo topics `claude-skills`, `claude-code-skill`
- [ClawHub](https://clawhub.ai/agenticweb4/skills/personal-knowledge-architect)
