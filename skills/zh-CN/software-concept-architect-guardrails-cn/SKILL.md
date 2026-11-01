---
name: software-concept-architect-guardrails-cn
description: "Validates concept specifications. Use when explicitly invoked. 检查、维护或映射概念与同步规格。"
compatibility: "读写与搜索文件；可选 Claude Code hooks 需要 bash 和 jq。"
metadata:
  language: zh-CN
  translation_of: software-concept-architect-guardrails
  author: ontology-of-everything
  version: "1.1.1"
  openclaw:
    homepage: https://github.com/ontology-of-everything/concept-skills
---

# 软件概念架构师 · 规格护栏

## 目标

维护能说明契约、可与实现核对的规格。仅在显式调用 `$software-concept-architect-guardrails-cn` 时运行。
流程改编自 [wyx v0.26.0](https://github.com/jlifyio/wyx)，保留 LICENSE.upstream，规格采用本仓记法。

## 原则

区分事实、推定目的、建议与未决。报告缺陷，不将缺陷转录为合法契约。同步遵守概念契约，产品依赖须有需求依据。

每个元素一份权威文件。概念所属 PIPELINE 与 CONCEPT 共置，跨概念管道放 composition，每个组合模块一份 SYNCS，内部按 flow 分组。
构建单元不自动成为概念。

audit 与 drift 不改规格和代码，只有明确要求时才保存检测历史。发现阶段只列候选，授权新建或修复在写入模式完成。
保留人工备注与旧行为，只确认未决模型取舍或扩大的范围。

## 概念

| 文件 | 职责 |
| --- | --- |
| CONCEPT | 概念的目的、状态、动作和运作原理 |
| SYNCS | 应用实例、类型绑定和因果同步规则 |
| PIPELINE | 数据来源、转换、质量规则与读写边界 |
| ARCHITECTURE | 从规格派生的导航，不是权威契约 |

回填从已读实现重建契约。漂移检测比较实现与已确认契约。两者都不证明设计能满足实际需要。

## 流程

1. 读工程约定、PRD 索引和相关规格，选择下表一种模式。缺规格或模式不明时先 audit。
2. 写入模式中，路径指定待检查实现，描述指定拟定行为。无目标时只发现候选。
3. 读所选模式参考，写 CONCEPT/SYNCS 或查管道接口前读[规格契约](references/spec-format.md)。
4. 完成检查或授权修改，更新索引，并按内容重建受影响地图。

| 模式 | 产出与必读参考 |
| --- | --- |
| `audit` | [覆盖与修复计划](references/audit.md) |
| `concept` | [候选或 CONCEPT](references/concept.md) |
| `drift` | [对比报告](references/drift-detection.md) |
| `pipeline` | [候选或 PIPELINE](references/pipeline.md) |
| `sync` | [候选或 SYNCS](references/sync.md) |
| `map` | [派生地图](references/map.md) |

只有要求安装 hooks 时才读[安装说明](references/hooks-runtime.md)。hooks 提示规格与可能陈旧的地图，不验证行为。

## 正反例

| 正例 | 反例 |
| --- | --- |
| audit 将协议适配器归为支撑代码，并记录依据。 | 为每个构建模块生成 CONCEPT，或在只读审计中改文件。 |

## 完成条件

说明范围、证据、未解析引用与未核实项。回填标注推断，地图指向当前规格。
模型取舍交设计，确认模型转录交 PRD，目的与组合审查交审查技能。技能不可用时说明所需工作。
