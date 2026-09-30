# 漂移检测（`drift` 模式）

焦点：已确认契约与当前行为哪里不同？漂移是两者的可证实差异，不是目的适切性的判断。全程只读；后续修复单独按授权执行。旧格式列待迁移。

## 取证

读范围内三类规格、PRD 暂存索引、祖先契约及相关外部 sync/管道，再逐份对照实现、schema/迁移和测试。多语言实现分别对账同一权威契约；范围外未读代码明确标出。

每个适用类别返回通过/发现/未核实；未读到实现不能证明不存在。规格多可委派只读小组或分批，传入检查表、校准和项目约定；聚合核对漏项、跨组引用和重要证据。

## CONCEPT.md

| 类别 | 判定依据 | 默认严重度 |
| --- | --- | --- |
| Missing action | 未记录的公开动作；排除内部辅助函数 | Medium |
| Removed action | 已声明动作在当前全部相关实现中不存在 | High |
| Changed signature | 参数、实际返回、错误分支改变契约 | Medium |
| New state | 未记录且影响可观察行为的状态；检查迁移/schema | Medium |
| Boundary violation | 绕过其他概念动作/query 访问其内部状态或实现 | High |
| Cross-cutting parameter | 多个动作的公共参数影响权限、身份等契约却未记录 | Medium |
| Spec naming violation | 四节真正依赖别的概念定义，或混入 interactions / dependencies 等边界段 | Medium |
| Intrinsic coupling | 概念直接调用另一概念的公开 API | High |
| OP 无测试 | principle 的场景无对应行为测试 | Medium |
| 排除动作被使用 | 应用有意排除的动作被调用或暴露 | High |
| Resolved known gap/coupling | 现有实现已解决记录在案的缺口 | Low |

业务协调归 SYNCS，产品依赖归总体 PRD；CONCEPT 不补 dependencies 段。局部参数同名合法。OP 缺测试属于验证缺口；已读契约支持 OP 却无法兑现目的时，记录设计问题并交 software-concept-architect-review-cn，不能靠补测试修复。

## PIPELINE.md

| 类别 | 判定依据 | 默认严重度 |
| --- | --- | --- |
| Missing stage | 影响数据契约的新增阶段未记录 | Medium |
| Changed invariant | 当前转换与已声明不变量矛盾 | High |
| New data source | 未声明的表/API/文件输入 | Medium |
| Boundary violation | 跨概念绕过公开接口读写私有数据 | High |

自身存储适配器内的 SQL 不是越界；外部输入不必虚构成概念拥有的表。

## SYNCS.md

| 类别 | 判定依据 | 默认严重度 |
| --- | --- | --- |
| Missing/Removed sync | 新协调未记录 / 已声明协调无实现 | Medium / High |
| Changed trigger | when 与实现的触发不同 | Medium |
| New participant | 实际参与概念未声明 | High |
| Changed binding/effect | where 的资格/绑定或 then 的目标/参数改变 | High |
| Graph inconsistency | 存在的派生图与规则块不符 | Medium |

同步图可在总体 PRD，不要求 SYNCS 内重复一份。响应、错误、循环等语义缺陷需要全面检查时交接 `software-concept-architect-review-cn`。

## 跨规格引用

逐条解析 include 实例化、动作、query、参数和输出 case，核对真实声明；`principle` / `operational principle` 视为同一节。`Requesting` 等明确的外部入口契约单独核对，不要求伪概念拥有 CONCEPT.md。

| 类别 | 判定依据 | 默认严重度 |
| --- | --- | --- |
| Missing reference | sync/管道引用不存在的动作或 query | High |
| Missing participant | 内部概念既无规格也无索引说明 | Medium |
| Signature/binding mismatch | 参数、输出 case 或类型实例化不匹配 | High |

## 校准

严重度为本仓约定，表值按可复现影响调整并说明：Critical 需权限绕过、数据破坏或核心不可用证据；High 为明确违约；Medium 为有影响遗漏；Low 为文档维护。

- 规格沉默不推出禁止，遗漏与矛盾分开；无语义变化的 Result/异步包装、私有派生值及显式命名映射不算违约。
- Medium 以上须当前规格/代码位置和证据；相同根因合并并列受影响路径，未执行类别不算通过。
- 架构例外注明来源、范围与后果；记录在案不消除实际风险。概念公开 API 互调仍破坏独立性，组合层调用合法。

## 报告与修复

```text
# Drift Report — <日期>
范围/规格与代码版本：...
Summary: 扫描 N；有漂移 N；Critical N / High N / Medium N / Low N
| 类别 | 规格位置 | 实现证据 | 影响/严重度 | 修复方向 |
跨规格引用：...
系统性模式：...（保留全部受影响路径）
未核实：...
建议的下一步：...
```

模型不合理 → design；文档陈旧 → prd/本技能；代码违约 → implementation。两侧冲突且不能从已确认需求判断时，呈现具体取舍后询问；不能默认让规格追随代码。已授权修复则报告后完成最小改动并重查；未授权则停在报告。

## 可选历史

只有用户要求时才追加 `.claude/wyx-drift-history.jsonl`，只读扫描不写。

```text
{"ts":"<ISO-8601>","action":"detect","specs_scanned":0,"specs_with_drift":0,"critical":0,"high":0,"medium":0,"low":0,"low_by_spec":{},"path":"<范围>"}
{"ts":"<ISO-8601>","action":"fix","specs_fixed":0,"specs_remaining":0,"ref_ts":"<对应 detect ts>"}
```

数字替换为实测；仅全部问题解决的规格计入 fixed，fix 关联所修 detect，不改旧行。无 action 的旧记录按 detect 理解。SessionStart 只读最后快照，局部扫描不代表全仓；重新扫描才可清除陈旧提示，不能伪造零漂移。Low 数量不自动升级严重度。

格式核对按 [统一规格契约](spec-format.md)：字段名、类型/基数、初态及输出分支均是契约；旧标题/签名本身不算漂移。公开抽象状态读取合法，私有表访问另判；成功空模式、then 漏填输入、同 flow 配错对象须以可达行为确定影响。
