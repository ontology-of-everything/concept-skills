# concept-skills

[![skills.sh](https://skills.sh/b/ontology-of-everything/concept-skills)](https://skills.sh/ontology-of-everything/concept-skills)

> 先说清含义，再写代码、跑命令、起草规格。

[concept-skills](https://github.com/ontology-of-everything/concept-skills)
提供 11 项能力、22 个中英文
[Agent Skills](https://agentskills.io/)，覆盖本体、语义层、概念设计与可视化学习。英文使用基础名，简体中文统一增加
`-cn`。

Cloud 操作类技能现已迁移到
[`concept-git/cloud-concept-skills`](https://github.com/concept-git/cloud-concept-skills)，本仓库不再分发。

办公类技能现已迁移到同级 `myoffice-skills` 仓库，本仓库不再分发。

概念设计几个技能改编自 Daniel Jackson 的 concepts 与 synchronizations 模型 ——
[The Essence of Software](https://essenceofsoftware.com/)（2021），sync 采用 _Beyond
Objects_（[arXiv:2606.27258](https://arxiv.org/abs/2606.27258)）里现行的 when/where/then 记法 —— 面向 Agent 改编，未获作者背书。

English: [README.md](README.md)。

当前版本为 **2.7.1**。概念设计工作流、`show-me-the-design` 与 `settle-the-concept-design` 仅显式调用；`read-it-reframe-it-own-it` 支持自动匹配；全部概念技能在 Codex 中需显式调用；`concept-guard` 只消费 Jackson 记法。

## 目录

- [技能](#技能)
- [安装](#安装)
- [用法](#用法)
- [经典使用案例](#经典使用案例)
- [贡献](#贡献)
- [更新日志](CHANGELOG.zh.md)
- [许可](#许可)

## 技能

<!-- skill-catalog:start -->

按主要解决的问题分类；系列名称用于展示。

### 概念设计

设计软件概念、职责、规格与实现。

| 技能 | 版本 | ClawHub 分类 |
| --- | --- | --- |
| [整理概念方案](skills/zh-CN/settle-the-concept-design-cn/SKILL.md) | 0.1.5 | development, knowledge |
| [设计软件概念](skills/zh-CN/concept-design-cn/SKILL.md) | 1.0.2 | development |
| [编写概念规格](skills/zh-CN/concept-prd-cn/SKILL.md) | 1.1.2 | development |
| [实现概念模型](skills/zh-CN/concept-build-cn/SKILL.md) | 1.1.2 | development |
| [审查概念设计](skills/zh-CN/concept-review-cn/SKILL.md) | 1.1.2 | development |
| [维护概念规格](skills/zh-CN/concept-guard-cn/SKILL.md) | 1.1.2 | development |
| [精炼现有概念](skills/zh-CN/concept-refine-cn/SKILL.md) | 1.0.2 | development |
| [图解软件概念](skills/zh-CN/show-me-the-design-cn/SKILL.md) | 0.2.2 | knowledge |

### 语义建模

定义数据、事实、维度与关系的业务含义。

| 技能 | 版本 | ClawHub 分类 |
| --- | --- | --- |
| [数据知识架构师](skills/zh-CN/data-knowledge-architect-cn/SKILL.md) | 1.1.0 | knowledge |

### 知识管理

从原文萃取、关联、组织和复用知识。

| 技能 | 版本 | ClawHub 分类 |
| --- | --- | --- |
| [个人知识架构师](skills/zh-CN/personal-knowledge-architect-cn/SKILL.md) | 0.4.0 | knowledge |

### 学习方法

围绕学习目标与关键框架建立并修正理解。

| 技能 | 版本 | ClawHub 分类 |
| --- | --- | --- |
| [读它，重构它，化为己有](skills/zh-CN/read-it-reframe-it-own-it-cn/SKILL.md) | 0.2.0 | knowledge |

<!-- skill-catalog:end -->

### 概念设计工作流

目的驱动的软件设计。基于 Daniel Jackson《The Essence of Software》的概念设计方法。

从需求到模块，以概念模型为契约。每个技能停在自己的边界上交棒：`design` → `prd` / `build` →
`review`。

共同原则：同步可收窄行为，不可扩展概念契约；组合合法性与目的兑现分别检验。

技能详情与分类见 [catalog.yml](catalog.yml)，本地化规范见 [CLAUDE.md](CLAUDE.md)。

## 安装

需要 Node.js 22.20+ 与 Git。在目标项目目录运行下列命令，直接复制即可；默认安装到当前项目的 Codex，不修改全局技能。

`--agent codex` 可换为 `--agent claude-code` 或 `--agent cursor`；增加 `--global` 可供所有项目使用。技能安装器的[参数说明](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)。

### 中文版

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill data-knowledge-architect-cn personal-knowledge-architect-cn concept-design-cn concept-prd-cn concept-build-cn concept-review-cn concept-guard-cn concept-refine-cn read-it-reframe-it-own-it-cn show-me-the-design-cn settle-the-concept-design-cn --agent codex --copy --yes
```

### 英文版

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill data-knowledge-architect personal-knowledge-architect concept-design concept-prd concept-build concept-review concept-guard concept-refine read-it-reframe-it-own-it show-me-the-design settle-the-concept-design --agent codex --copy --yes
```

### 按需安装单个技能

**`data-knowledge-architect-cn`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill data-knowledge-architect-cn --agent codex --copy --yes
```

**`personal-knowledge-architect-cn`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill personal-knowledge-architect-cn --agent codex --copy --yes
```

**`concept-design-cn`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill concept-design-cn --agent codex --copy --yes
```

**`concept-prd-cn`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill concept-prd-cn --agent codex --copy --yes
```

**`concept-build-cn`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill concept-build-cn --agent codex --copy --yes
```

**`concept-review-cn`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill concept-review-cn --agent codex --copy --yes
```

**`concept-guard-cn`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill concept-guard-cn --agent codex --copy --yes
```

**`concept-refine-cn`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill concept-refine-cn --agent codex --copy --yes
```

**`read-it-reframe-it-own-it-cn`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill read-it-reframe-it-own-it-cn --agent codex --copy --yes
```

**`show-me-the-design-cn`**

```bash
npx --yes skills add ontology-of-everything/concept-skills --skill show-me-the-design-cn --agent codex --copy --yes
```

### 查看可安装技能

```bash
npx --yes skills add ontology-of-everything/concept-skills --list
```

英文载荷位于 `skills/en/`，简体中文载荷位于 `skills/zh-CN/`；中文技能名仍以 `-cn` 结尾。ClawHub 发布概念设计系列的中英文版，中文技能名保留 `-cn`。

## 用法

技能通常按 description 自动触发，正常说话就够。概念设计工作流默认不启动，必须显式指名（Cursor
`/concept-design`，Codex `$concept-design`）：

```text
$concept-design-cn 把这个需求建成概念模型
$concept-prd-cn 模型定了，出一份 PRD 规格
$concept-guard-cn concept src/orders
$concept-guard-cn drift src/orders
$show-me-the-design-cn 用一张小图解释当前概念模型
把这套接口做成语义层                        → data-knowledge-architect-cn
```

要指名某个技能：Cursor 里用 `/skill-name`，Codex 里用 `$skill-name`。

## 经典使用案例

每项技能保留两个例子。先安装技能、提供相关材料，再复制一句试试。示例路径换成你自己的项目路径。

### 整理概念方案

`settle-the-concept-design-cn` · [技能正文](skills/zh-CN/settle-the-concept-design-cn/SKILL.md)

基于 Daniel Jackson 的概念设计，综合讨论收敛待确认的决策，从目标与概念目的总览，逐步展开场景和决策所需规格。

| 场景 | 可以这样说 |
| --- | --- |
| 收敛设计 | `$settle-the-concept-design-cn` 综合我们的全部讨论，整理待确认的概念设计，列明选择、理由与未决事项。 |
| 核对变更 | `$settle-the-concept-design-cn` 对照已确认设计，说明本轮改了什么、为什么改，以及对业务目标和验收的影响。 |

### 读它，重构它，化为己有

`read-it-reframe-it-own-it-cn`

| 场景 | 可以这样说 |
| --- | --- |
| 整理笔记 | `$read-it-reframe-it-own-it-cn` 帮我把这些概念设计笔记整理成知识树，方便我复习。 |
| 画学习笔记图 | `$read-it-reframe-it-own-it-cn` 把这棵知识树画成中文学习笔记图。 |

第二个例子还需要搭配图片生成工具。[ClawHub 英文版](https://clawhub.ai/agenticweb4/skills/learning-read-it-reframe-it-own-it)使用独立地址；本仓库的技能安装名不变。

### 图解软件概念

`show-me-the-design-cn` · [使用说明与可视化工具箱](skills/zh-CN/show-me-the-design-cn/SKILL.md)

以源码为依据，从整体到局部图解软件概念与协作，帮助零基础读者理解和审视设计。随包设计参考提供可复用的 HTML、CSS 与 JavaScript。

| 场景 | 可以这样说 |
| --- | --- |
| 理解设计 | `$show-me-the-design-cn` 探索项目，用图解讲清概念边界与动作协作。 |
| 核对实现 | `$show-me-the-design-cn` 对照这份设计与源码，解释差异及其影响。 |

### 个人知识架构师

`personal-knowledge-architect-cn`

| 场景 | 可以这样说 |
| --- | --- |
| 找可复用的方法 | `$personal-knowledge-architect-cn` 帮我整理这些访谈笔记，先列出能复用的方法，给我看看。 |
| 整理方法库 | `$personal-knowledge-architect-cn` 把这些产品研究笔记整理成方法库，相同的方法合并一下。 |

### 数据知识架构师

`data-knowledge-architect-cn`

| 场景 | 可以这样说 |
| --- | --- |
| 看懂数据表 | `$data-knowledge-architect-cn` 帮我看看这张订单表，哪些是事实、维度和度量？ |
| 整理接口模型 | `$data-knowledge-architect-cn` 把这组订单接口整理成语义模型，确认后输出 OKF。 |

### 设计软件概念

`concept-design-cn`

| 场景 | 可以这样说 |
| --- | --- |
| 设计待办清单 | `$concept-design-cn` 帮我设计一个待办清单，支持添加、完成和重新打开。 |
| 设计预约与候补 | `$concept-design-cn` 餐厅预约满了还能排队，帮我理清需要哪些概念、怎么配合。 |

### 编写概念规格

`concept-prd-cn`

| 场景 | 可以这样说 |
| --- | --- |
| 整理 PRD | `$concept-prd-cn` 把确认好的待办模型整理成一份简明 PRD。 |
| 补齐规格 | `$concept-prd-cn` 给这个预约系统补上 CONCEPT.md 和 SYNCS.md，按已确认的设计来。 |

### 实现概念模型

`concept-build-cn`

| 场景 | 可以这样说 |
| --- | --- |
| 实现待办清单 | `$concept-build-cn` 按确认好的待办模型，用 TypeScript 实现一下，顺便测测。 |
| 实现预约与取消 | `$concept-build-cn` 把餐厅预约和取消做出来，按现有规格写，并验证流程。 |

### 审查概念设计

`concept-review-cn`

| 场景 | 可以这样说 |
| --- | --- |
| 检查概念模型 | `$concept-review-cn` 帮我看看这个待办模型有没有问题，先别改。 |
| 检查代码偏差 | `$concept-review-cn` 对照规格检查预约代码，看看有没有写偏，给我指出来。 |

### 维护概念规格

`concept-guard-cn`

| 场景 | 可以这样说 |
| --- | --- |
| 盘点缺少的规格 | `$concept-guard-cn` audit src/reservations 这里缺哪些规格？帮我列一下。 |
| 检查规格漂移 | `$concept-guard-cn` drift src 对照现有规格看看代码有没有写偏，先别改。 |

### 精炼现有概念

`concept-refine-cn`

| 场景 | 可以这样说 |
| --- | --- |
| 理清职责 | `$concept-refine-cn` 这个 Todo 又管任务又发提醒，要不要拆开？帮我看看。 |
| 比较相似概念 | `$concept-refine-cn` 收藏和稍后阅读要分开吗？结合使用场景说说。 |

**串联使用：** 设计并确认模型 → PRD → 实现 → 审查。已有项目可先运行 Guardrails audit，再根据问题补规格或精炼概念。

每个阶段都可搭配 `show-me-the-design-cn`，直观解释当前模型或实现。

## 贡献

`qa/` 仅供本机使用，不提交、不发布；公开校验不依赖它。需要运行本机用例时，使用 `./tools/validate-all.sh --local-qa`。

项目职责与目录规范见 [CLAUDE.md](CLAUDE.md)。

```bash
git config core.hooksPath .githooks
./tools/validate-all.sh
```

`skills/en/<name>/` 与 `skills/zh-CN/<name>-cn/`
是自包含安装载荷；本机校验不进入仓库。每次修改须同步中英文、公开目录、说明文档与一致性检查。

## 许可

[Apache-2.0](LICENSE) © concept-skills contributors。发布到 [ClawHub](https://clawhub.ai/)
的技能包在该平台为 MIT-0；仓库源码仍为 Apache-2.0。
