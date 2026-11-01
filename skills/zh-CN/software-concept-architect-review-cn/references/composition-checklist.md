# 组合缺陷检查表

先查应用目的与场景，再查概念选择、SYNCS 和实际 mediator/引擎及适配器。
完成匹配、绑定、关联和公开状态读取按[规格契约](spec-format.md)核对。

| 类别 | 需要的证据 | 默认严重度 | 路由 |
| --- | --- | --- | --- |
| 行为保持违规 | 组合执行中某概念的动作/状态/输出序列违反自身契约；仅减少允许行为不算违约 | High | implementation；模型缺契约则 design |
| 隐式组合 | 概念 A 内直接调用 B，包含公开 API 互调 | High | implementation |
| 错误/响应缺口 | 可达结果无处理策略，或需要响应的请求会悬挂/串请求 | High | design / implementation |
| 绑定错误 | then 使用未绑定或未来输出；零/多 query 结果处理不符契约 | High | design / implementation |
| 合取/关联错误 | 多 when 变任一触发、跨请求匹配或同 flow 内配错对象 | High | design / implementation |
| 结果匹配错误 | 空输出模式当成功，或把 valid=false 当 error，导致可达错误调用 | High | design / implementation |
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
| 组合偏离目的 | 组合扭曲概念原 purpose，并有用户场景 | Medium | design |

按[严重度校准](drift-checklist.md#严重度校准)判断。类型级环、没有深度上限、流程长、规则分散、后台无 HTTP 响应或持久日志，本身都不是缺陷。
须检查实际行为。动作发生图可能在重复触发时仍无环，有向无环图也不证明终止。

结果可按契约响应、重试、补偿或有意忽略，不要求每种输出单独一条错误规则。
检查全部支持入口后才能判定规则不可达，未读路径标未核实。查询访问合法也不证明系统性质或进展。

独立性、漂移与组合中的同一根因合并报告，保留当前位置、行为证据、用户后果与当前修复步骤。
