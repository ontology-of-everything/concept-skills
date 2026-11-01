# 规格漂移与严重度

连同当前实现、schema/迁移、测试和 PRD 暂存文件读取规格。
旧记法、签名、基数、结果分支和可达匹配以[规格契约](spec-format.md)核对，查询不产生完成事件。
运作原理缺测试是验证缺口，目的论证失败须附反例。无代码时不判断实现或测试覆盖。

## 类别

| 对象/类别 | 判定依据 | 默认严重度 |
| --- | --- | --- |
| CONCEPT / Missing action | 未声明的公开动作 | Medium |
| Removed action | 已声明动作在全部相关实现中不存在 | High |
| Changed signature | 入参、真实返回或错误 case 改变契约 | Medium |
| New state | 未声明且影响可观察行为的状态 | Medium |
| Spec naming violation | Jackson 四节依赖其他概念定义；同名局部参数合法 | Medium |
| Boundary violation | 绕过其他概念公开接口访问其内部状态/实现 | High |
| Intrinsic coupling | 概念直接调用另一概念公开 API | High |
| Cross-cutting parameter | 影响契约的公共参数未记录 | Medium |
| OP 无测试 | 代表性故事无对应行为测试 | Medium |
| 排除动作被使用 | 明确排除的应用动作实际可达 | High |
| SYNCS / Missing/Removed sync | 新增协调未记录 / 旧规则无实现 | Medium / High |
| Changed trigger | when 与真实触发不同 | Medium |
| Changed binding/effect | where 资格/绑定或 then 目标/参数改变 | High |
| New participant | 实际参与概念未声明 | High |
| Graph inconsistency | 存在的派生图与规则不符 | Medium |
| 跨规格 / Missing reference | sync 动作/query 无声明，或签名/实例化不匹配 | High |
| Missing participant | 内部概念无规格或索引 | Medium |

外部入口仍须核对参数、结果与关联，Requesting 不必有虚构的 CONCEPT。
PIPELINE 遗漏阶段/来源默认为 Medium，不变量矛盾或私有访问为 High。
同步图可只放总体 PRD，产品依赖须有需求证据。

## 严重度校准

Critical 须有权限绕过、数据破坏或核心不可用证据。High 为明确违约，Medium 为有影响遗漏，Low 为局部维护。
按可复现影响调整默认值并说明，Low 数量不自动升级严重度。

规格沉默不证明禁止。私有辅助函数、派生缓存、保持行为的 Result/异步包装和命名映射本身不是漂移。
公开抽象状态可合法读取。例外须记录范围与后果，记录概念互调不表示独立性恢复。

## 证据与范围

工程约定与语义漂移分别检查。采用默认模块单体时，核对独立构建测试、同进程公开工厂装配、
api/composition/concept 边界、概念独立性和向内依赖。目录或无环图不证明源码访问合法，也不证明行为正确。
不将默认结构追溯为旧项目要求。

Medium 及以上附当前位置。搜索未命中不能证明不存在，未读路径标未核实。
相关规格分批检查，每类返回通过/发现/未核实，再核对跨规格引用，合并同一根因并列受影响路径。
