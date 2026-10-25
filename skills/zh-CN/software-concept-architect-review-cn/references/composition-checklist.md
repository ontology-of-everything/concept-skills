# 组合缺陷检查表

先从总体 PRD/需求定位应用目的与端到端场景，再检查概念选择、SYNCS 和已有的 mediator/引擎及接口适配器。采用 WYSIWID 因果语义：when 匹配完成事件，where 产生绑定，then 发起调用；多 when 保持同 flow，错误须有声明。where 可读公开抽象状态或声明 query，物理存储仍受边界保护；详细匹配规则见 [规格契约](spec-format.md)。

| 类别 | 需要的证据 | 默认严重度 | 路由 |
| --- | --- | --- | --- |
| 行为保持违规 | 组合执行中某概念的动作/状态/输出序列违反自身契约；仅减少允许行为不算违约 | High | implementation；模型缺契约则 design |
| 隐式组合 | 概念 A 内直接调用 B，包含公开 API 互调 | High | implementation |
| 错误/响应缺口 | 可达结果无处理策略，或需要响应的请求会悬挂/串请求 | High | design / implementation |
| 绑定错误 | then 使用未绑定或未来输出；零/多 query 结果处理不符契约 | High | design / implementation |
| 合取/关联错误 | 多 when 变任一触发、跨请求匹配或同 flow 内配错对象 | High | design / implementation |
| case 匹配错误 | 空输出模式当成功，或把 valid=false 当 error，导致可达错误调用 | High | design / implementation |
| 冲突 sync | 可共同触发的效果造成可复现的不合法结果/顺序依赖 | High | design |
| 重放缺陷 | 重复匹配/投递造成不允许的重复副作用 | High | implementation |
| 死 sync | 证明所有支持入口均无法产生其触发事件 | Low | prd / design |
| 级联无界 | 可达循环持续产生新动作且无终止或受控运行策略 | High | design / implementation |
| 欠/过同步 | 应用场景证明目的落空：漏联动或控制被自动化夺走 | Medium | design |
| 不变量错位 | 只在组合查询校验本应由概念动作原子保持的不变量 | High | implementation |
| sync 自有业务状态 | 编排积累独立目的及业务生命周期 | Medium | design |
| 直通动作 | API 绕过已确认认证/协调约束；补充实际影响 | High | implementation |
| 排除动作被使用 | 有应用级明确排除决策，实际路径仍可达 | High | implementation / design |
| 图/规格不符 | 派生图丢失合取、查询/触发混淆或引用错误 | Medium | prd |
| synergy 反噬 | 组合扭曲概念原 purpose，并有用户场景 | Medium | design |

采用 [漂移校准](drift-checklist.md#严重度校准)。以下不单独构成缺陷：类型级图成环、未设 depth limit、flow 触达 ≥5 个概念、规则分散目录、后台无 HTTP 响应、运行时持久日志。检查实际行为及本项目约定；循环发生图可以仍是 DAG，DAG 也不保证终止。

错误可响应、重试、补偿或有意忽略，不强制每种输出各一条错误 sync。完整读过支持入口后才能判死规则；未扫描的路径标未核实。查询接口合法也不自动保证系统性质或活性。

同一根因在独立性/漂移/组合检查重复时合并；报告保留来源位置、行为证据、用户后果和唯一的当前修复步骤。
