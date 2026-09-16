# concept-skills

[![skills.sh](https://skills.sh/b/ontology-of-everything/concept-skills)](https://skills.sh/ontology-of-everything/concept-skills)

> 先说清含义，再写代码、跑命令、起草规格。

[concept-skills](https://github.com/ontology-of-everything/concept-skills)
提供 7 项能力、14 个中英文
[Agent Skills](https://agentskills.io/)，覆盖本体与语义层和概念设计。英文使用基础名，简体中文统一增加
`-cn`。

华为云操作类技能现已迁移到
[`concept-git/cloud-concept-skills`](https://github.com/concept-git/cloud-concept-skills)，本仓库不再分发。

办公类技能现已迁移到同级 `myoffice-skills` 仓库，本仓库不再分发。

概念设计几个技能改编自 Daniel Jackson 的 concepts 与 synchronizations 模型 ——
[The Essence of Software](https://essenceofsoftware.com/)（2021），sync 采用 _Beyond
Objects_（[arXiv:2606.27258](https://arxiv.org/abs/2606.27258)）里现行的 when/where/then 记法 —— 面向 Agent 改编，未获作者背书。

English: [README.md](README.md)。

当前版本为 **1.1.0**。`concept-*` 全家仅显式调用；`concept-guardrails` 只消费 Jackson 记法。

## 目录

- [技能](#技能)
- [安装](#安装)
- [用法](#用法)
- [贡献](#贡献)
- [更新日志](CHANGELOG.zh.md)
- [许可](#许可)

## 技能

### 概念设计

从需求到模块，以概念模型为契约。每个技能停在自己的边界上交棒：`design` → `prd` / `implementation` →
`audit`。

| 技能                                                                       | 版本   | 做什么                             |
| -------------------------------------------------------------------------- | ------ | ---------------------------------- |
| [`concept-design-cn`](docs/skills/cn/concept-design-cn.md)                 | 0.7.0  | 设计独立概念与同步组合             |
| [`concept-prd-cn`](docs/skills/cn/concept-prd-cn.md)                       | 0.6.0  | 转录确认模型并保留验收追溯         |
| [`concept-implementation-cn`](docs/skills/cn/concept-implementation-cn.md) | 0.7.0  | 实现独立概念模块与同步组合         |
| [`concept-audit-cn`](docs/skills/cn/concept-audit-cn.md)                   | 0.6.0  | 只读审查设计论证、漂移和实现符合性 |
| [`concept-guardrails-cn`](docs/skills/cn/concept-guardrails-cn.md)         | 0.31.0 | 创建、审查和映射共存规格           |

### 本体与语义

企业知识来自 API / 数据库（`semantic-km-creator`）；个人知识来自原文（`semantic-pkm-creator`）。

| 技能                                                                   | 版本  | 做什么                          |
| ---------------------------------------------------------------------- | ----- | ------------------------------- |
| [`semantic-km-creator-cn`](docs/skills/cn/semantic-km-creator-cn.md)   | 0.6.0 | 从接口建立证据化 Kimball 语义层 |
| [`semantic-pkm-creator-cn`](docs/skills/cn/semantic-pkm-creator-cn.md) | 0.3.0 | 从原文萃取场景、概念和实体      |

英文技能说明位于 `docs/skills/en/`，中文说明位于 `docs/skills/cn/`。机器可读索引见
[docs/catalog.yml](docs/catalog.yml)，本地化规范见 [docs/localization.md](docs/localization.md)。

## 安装

需要 Node.js（用于 `npx`）。

基础名安装英文版；简体中文版统一使用 `-cn`。

ClawHub 只发布 `skills/en` 英文版；中文版继续通过 GitHub 安装。

```bash
npx skills add ontology-of-everything/concept-skills \
  --skill <skill-name> \
  --agent cursor \
  --copy -y
```

`--agent` 可填 `cursor`、`claude-code` 或 `codex`。一次装多个；加 `--global` 装到
`~/.agents/skills/`（Cursor 与 Codex 都会扫描），而不是项目的 `.agents/skills/`：

```bash
npx skills add ontology-of-everything/concept-skills \
  --skill concept-design concept-prd concept-guardrails \
  --agent cursor codex \
  --global --copy -y
```

列出可装技能，或开发时从本地目录安装：

```bash
npx skills add ontology-of-everything/concept-skills --list
npx skills add ./skills/<skill-name> --skill <skill-name> --agent cursor --copy -y
```

收录：[skills.sh](https://skills.sh/ontology-of-everything/concept-skills)（分组见
[`skills.sh.json`](skills.sh.json)）·
[SkillsMP](https://skillsmp.com/)（仓库 topics：`claude-skills`、`claude-code-skill`）·
[ClawHub](https://clawhub.ai/)。

各 Agent 说明：[Cursor](docs/agents/cursor.md) · [Claude Code](docs/agents/claude-code.md) ·
[Codex](docs/agents/codex.md)。

使用前先读一遍技能内容——技能以你的 Agent 权限运行。

## 用法

技能通常按 description 自动触发，正常说话就够。`concept-*` 全家默认不启动，必须显式指名（Cursor
`/concept-design`，Codex `$concept-design`）：

```text
$concept-design-cn 把这个需求建成概念模型
$concept-prd-cn 模型定了，出一份 PRD 规格
$concept-guardrails-cn 给 src/orders 写概念规格，然后查漂移
把这套接口做成语义层                        → semantic-km-creator-cn
```

要指名某个技能：Cursor 里用 `/skill-name`，Codex 里用 `$skill-name`。

## 贡献

[docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) · [docs/authoring.md](docs/authoring.md)

```bash
./tools/skill-scaffold.sh <skill-name>   # 新建技能
./tools/install-git-hooks.sh             # pre-commit → validate-all.sh
./tools/validate-all.sh                  # 全部技能，与 CI 一致
./qa/<skill-name>/validate.sh            # 单个技能
```

`skills/en/<name>/` 与 `skills/cn/<name>-cn/`
是自包含安装载荷；QA 按相同语言目录分层且不随安装分发。每次修改必须同步中英文、目录、文档和 parity 门禁。

## 许可

[Apache-2.0](LICENSE) © concept-skills contributors。发布到 [ClawHub](https://clawhub.ai/)
的技能包在该平台为 MIT-0；仓库源码仍为 Apache-2.0。
