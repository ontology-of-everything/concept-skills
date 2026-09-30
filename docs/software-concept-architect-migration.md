# Software Concept Architect：命名与 ClawHub 迁移

日期：2026-09-30。系列副标题：**Purpose-Driven Software Design**。

## 名称与展示标题

ClawHub 使用完整英文展示标题；Agent UI 使用简短展示名和收益短描述。`docs/catalog.yml` 保存二者。中文包统一增加 `-cn`，仅通过 GitHub/本地安装分发。

| 原名称 | 最终英文名称 | 展示名 | 展示标题 |
| --- | --- | --- | --- |
| `concept-design` | `software-concept-architect-design` | Software Concept Architect · Design | Software Concept Architect · Design — Turn Requirements into Clear Concepts |
| `concept-prd` | `software-concept-architect-prd` | Software Concept Architect · PRD | Software Concept Architect · PRD — Turn Models into Traceable Specs |
| `concept-implementation` | `software-concept-architect-build` | Software Concept Architect · Build | Software Concept Architect · Build — Turn Models into Independent Modules |
| `concept-audit` | `software-concept-architect-review` | Software Concept Architect · Review | Software Concept Architect · Review — Find Design Gaps and Code Drift |
| `concept-refine` | `software-concept-architect-refine` | Software Concept Architect · Refine | Software Concept Architect · Refine — Untangle Overloaded Concepts |
| `concept-guardrails` | `software-concept-architect-guardrails` | Software Concept Architect · Guardrails | Software Concept Architect · Guardrails — Keep Specs and Code Aligned |

| 中文展示名 | 中文展示标题 |
| --- | --- |
| 软件概念架构师 · 设计 | 软件概念架构师 · 设计 — 把需求变成清晰的软件概念 |
| 软件概念架构师 · 需求规格 | 软件概念架构师 · 需求规格 — 把确认的模型变成可追溯规格 |
| 软件概念架构师 · 实现 | 软件概念架构师 · 实现 — 把确认的模型落成独立模块 |
| 软件概念架构师 · 审查 | 软件概念架构师 · 审查 — 找出设计缺口与代码偏差 |
| 软件概念架构师 · 精炼 | 软件概念架构师 · 精炼 — 理清过载职责，精炼概念边界 |
| 软件概念架构师 · 规格护栏 | 软件概念架构师 · 规格护栏 — 让规格与代码保持一致 |

## 范围与内容保护

- 迁移 6 项能力、12 个中英文包，以及 QA 路径、调用引用、安装示例、目录、技能页和 UI 元数据。
- 方法、工作流、判据、参考资料与运行时逻辑保持当前本地版本；仅替换必要的技能名称与路径，更新标题和发布元数据。
- 5 项能力仍仅显式调用；Refine 保留自动匹配。
- 系列首次统一发布为 1.0.0。ClawHub 原有版本落后于本地，最终发布以本次更名前的本地内容为基线。
- Refine 移除与 ClawHub MIT-0 分发冲突的 frontmatter license 字段；仓库 Apache-2.0 和上游许可文件保留。
- 保留既有学习类未提交改动；不创建 Git 提交、Git 标签或 GitHub Release。
- 仓库主页链接保持有效；源文件路径迁移保留在本地，后续 Git 推送另行处理。

## 发布与历史清理

1. 通过内容等价检查、本地化门禁与全量 QA。
2. 将已有英文条目改为最终名称，保留下载统计与旧链接跳转；新增尚未发布的 Refine。
3. 上传最终 1.0.0，并核验远端标题、版本及文件校验值。
4. 仅当新版本可公开使用时，撤回该技能此前的全部版本。平台保留的旧链接仅用于跳转，不是独立旧版本。
5. 回读版本列表，确认只保留最终可用版本。

## 验证与执行结果

- 本地：12 个中英文安装包完成更名；94 个安装载荷文件通过内容等价核验，除名称、路径、标题和发布元数据外保持原内容。
- `tools/validate-all.sh` 全量通过，包含 9 对技能的本地化校验、规格副本一致性、Markdown 校验、技能格式与现有质量检查；描述长度/关键词评分仍有非阻断告警。
- Guardrails 的 ClawHub CLI 预检会跳过 `runtime/.claude-plugin/plugin.json`。最终通过同一官方发布 API 显式包含此文件，保留全部 16 个文件；许可文本 `LICENSE.upstream` 无需改名。
- 六个英文技能的 1.0.0 均已公开生效；远端标题、所有者、最终名称和 47 个载荷文件的逐文件 SHA-256 与本地一致（平台自动生成的 skill-card 不计入本地载荷）。
- 共撤回 20 个历史版本。最终回读确认六个条目的版本列表均只有 `1.0.0`；5 个原有名称解析到对应新名称，既有下载记录保留。Refine 为首次发布。
- 12 个迁移后的技能说明页及中英文 README 的本地链接检查通过。
- 平台扫描：Design、PRD、Build、Review、Refine 为 clean。Guardrails 已发布，但版本扫描为 suspicious / hasWarnings；提示原有可选 hooks 会将仓库规格文本自动注入 Agent 上下文，存在提示注入与范围披露方面的审查关注点。平台未阻止发布（isMalwareBlocked=false）。按“具体内容不变”的要求，本次未修改该功能。
- Git：此次未提交或推送；保留任务开始前已有的学习类未提交改动。

## 最终 ClawHub 条目

- [Software Concept Architect · Design — Turn Requirements into Clear Concepts](https://clawhub.ai/agenticweb4/skills/software-concept-architect-design) — `1.0.0`
- [Software Concept Architect · PRD — Turn Models into Traceable Specs](https://clawhub.ai/agenticweb4/skills/software-concept-architect-prd) — `1.0.0`
- [Software Concept Architect · Build — Turn Models into Independent Modules](https://clawhub.ai/agenticweb4/skills/software-concept-architect-build) — `1.0.0`
- [Software Concept Architect · Review — Find Design Gaps and Code Drift](https://clawhub.ai/agenticweb4/skills/software-concept-architect-review) — `1.0.0`
- [Software Concept Architect · Refine — Untangle Overloaded Concepts](https://clawhub.ai/agenticweb4/skills/software-concept-architect-refine) — `1.0.0`
- [Software Concept Architect · Guardrails — Keep Specs and Code Aligned](https://clawhub.ai/agenticweb4/skills/software-concept-architect-guardrails) — `1.0.0`
