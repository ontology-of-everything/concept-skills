# concept-skills

**让功能有边界，让协作看得见。**

加一个“分享”功能，常常要同时修改发帖、权限和通知代码。
关联藏在多处，改动会影响什么，很难直接看出来。

`concept-design` 用 Daniel Jackson 的概念与同步方法支持软件设计与 AI 编程。
从用户需要出发，划分独立模块、写明协作规则，再用于规格、实现、审查与 Mermaid 关系图。
规格采用 Daniel Jackson 的 Beyond Objects，工程执行参考 Meng 与 Jackson 的 WYSIWID。

## 怎么工作

- **概念**承载独立功能，拥有自己的状态和动作；概念之间不互调、不互读状态。
- **同步规则**写明协作：发生什么、满足什么条件、接着调用什么动作。
- **LLM 与 CLI**分工：LLM 按规格生成或修改代码，CLI 检查规格结构，审查与测试验证行为。

例如：评论创建完成 → 查询文章作者 → 发送通知。
协作写在同步规则里，评论概念不需要依赖通知概念。

## 解决什么

功能可以定位，概念可以单独改，协作规则可以直接读。
加功能之前，先复用概念或改几条同步规则，再核对原有行为是否还在。
方法见[参考资料](skills/zh-CN/concept-design-cn/SKILL.md#参考资料)。

## 开始使用

在本仓库目录安装一种语言。`--agent` 可换成 `claude-code` 或 `cursor`。

```sh
npx --yes skills add . --skill concept-design-cn --agent codex --copy --yes
```

英文把技能名换成 `concept-design`。点名调用。技能只读取当前任务要用的流程。

```text
$concept-design-cn design 为预约功能定义概念和同步规则。
$concept-design-cn build 实现已确认的规格。
$concept-design-cn review src/orders 只读检查概念边界与实现。
$concept-design-cn guard map src 生成概念与同步关系图。
```

还支持 settle、prd、guard、refine、explain；英文使用 `$concept-design`。

## concept-lint 检查什么

只读、零第三方依赖，检查本技能的 [工具编码](skills/zh-CN/concept-design-cn/references/tool-encoding.md)：

```sh
python3 skills/zh-CN/concept-design-cn/scripts/concept_lint.py CONCEPT.md SYNCS.md --json
```

检查声明与核心章节、when/then 完成与调用形状、顶层具名字段，以及本次输入中同一应用的规则名唯一性。
无法识别的调用记法返回未检查；类型、绑定、概念独立性和运行结果仍需其他证据。
退出码：`0` 通过所列检查，`1` 格式错误，`2` 读取/用法错误，`3` 未检查。

## 生成概念与同步关系图

扫描 CONCEPT.md 与 SYNCS.md，生成一份含概念索引、Mermaid 图、关系表和来源行号的 ARCHITECTURE.md。
概念定义、实例和同步规则分别编号；未解析引用保留为缺口。

```sh
python3 skills/zh-CN/concept-design-cn/scripts/concept_map.py <项目根> --output <项目根>/ARCHITECTURE.md
```

`--scope RELPATH` 缩小显示范围，`--check` 只读检查更新，已有文档只替换生成区。
具体约定见[图格式](skills/zh-CN/concept-design-cn/references/diagram-contract.md)。

## 仓库技能

每个技能有英文名和 `-cn` 版。用上面的命令，换成技能名即可。下面的总表按领域各写一行用途。各技能的范围是：

| 技能 | 范围 |
| --- | --- |
| `data-knowledge-architect-cn` | 数据、事实、维度和关系的业务含义。 |
| `personal-knowledge-architect-cn` | 从原文抽出可复用的方法、场景和实体。 |
| `read-it-reframe-it-own-it-cn` | 在一个学习目标和一个框架下建立知识树。 |
| `architect-4r-cn` | 用李运华的 4R 方法，从代码或讨论梳理现有架构。 |
| `architect-4c-cn` | Simon Brown 的 C4 模型：层级、原则和常见误用。 |
| `architect-frontend-feature-first-cn` | 功能优先的前端：能力归属和跨功能边界。 |
| `architect-frontend-fsd-cn` | Feature-Sliced Design：层、切片、片段、公开接口和依赖边界。 |
| `agent-dx-cli-cn` | 设计、审查和重构面向智能体的 CLI，并用可执行证据评分。 |

<!-- skill-catalog:start -->

| 技能 | 用途 | 版本 |
| --- | --- | --- |
| [Java 代码简化](skills/zh-CN/simplify-java-cn/SKILL.md) | 保留行为与有用边界，简化 Java / Spring Boot 代码。 | 0.2.1 |
| [概念建模原则](skills/zh-CN/concept-model-cn/SKILL.md) | 用概念定义独立功能，用同步规则定义概念之间的协作。 | 1.1.0 |
| [概念设计](skills/zh-CN/concept-design-cn/SKILL.md) | 用概念定义独立功能，用同步规则定义概念之间的协作。 | 2.5.1 |
| [数据知识架构师](skills/zh-CN/data-knowledge-architect-cn/SKILL.md) | 定义数据、事实、维度与关系的业务含义。 | 1.1.0 |
| [个人知识架构师](skills/zh-CN/personal-knowledge-architect-cn/SKILL.md) | 从原文萃取、关联、组织和复用知识。 | 0.4.0 |
| [读它，重构它，化为己有](skills/zh-CN/read-it-reframe-it-own-it-cn/SKILL.md) | 围绕学习目标与关键框架建立并修正理解。 | 0.2.0 |
| [4R 系统建模框架](skills/zh-CN/architect-4r-cn/SKILL.md) | 软件架构模型的核心概念、定义、原则与常见误用。 | 0.4.0 |
| [C4 软件架构模型](skills/zh-CN/architect-4c-cn/SKILL.md) | 软件架构模型的核心概念、定义、原则与常见误用。 | 0.1.0 |
| [功能优先前端架构](skills/zh-CN/architect-frontend-feature-first-cn/SKILL.md) | 软件架构模型的核心概念、定义、原则与常见误用。 | 0.1.0 |
| [前端 Feature-Sliced Design](skills/zh-CN/architect-frontend-fsd-cn/SKILL.md) | 软件架构模型的核心概念、定义、原则与常见误用。 | 0.1.0 |
| [面向智能体的 CLI 工程](skills/zh-CN/agent-dx-cli-cn/SKILL.md) | 以可预测性、纵深防御和上下文效率指导 CLI 设计、审查与重构。 | 0.4.3 |

<!-- skill-catalog:end -->

## 维护与许可

原八项概念设计流程共用一个入口，每种语言一份。概念设计版本为 **2.5.1**，仓库版本为 **3.8.1**。
ClawHub 旧入口能合并的已跳转，其余已下线或原本不可用；迁移时保留项目规格、源码和用户配置。

运行 `./tools/validate-all.sh` 检查公开安装包。
[仓库规则](CLAUDE.md) · [更新日志](CHANGELOG.zh.md) · [English](README.md)。
[Apache-2.0](LICENSE)。ClawHub 安装包使用 MIT-0。
