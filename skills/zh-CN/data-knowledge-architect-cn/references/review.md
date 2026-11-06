# Phase 2：决策评审

明确 brief（目标、交付物、范围、证据边界）、全局约束和原子问题，依次处理粒度、维度、
度量、指标与路由。每项决定区分来源基础（`explicit|inferred|missing`）、推荐置信度与用户反馈。
批准只改变反馈状态，不提高证据质量。缺证据必须补充或明确排除范围，不能靠选择看似合理的候选变成事实。

## 建立工作台

将 model JSON 替换 `assets/review-template.html` 的 `/*__MODEL_JSON__*/`。
用 JSON 序列化，嵌入前将 `<` 转义成 `\u003c`，防止来源内容关闭 script 元素。
不把来源字符串插入可执行 HTML/JavaScript。JSON 与报告同目录保存，作为权威输入。
选择用户可访问的输出目录，临时路径是可选项。模板离线运行，无自动回调，
用户须在聊天或文件中返回导出的反馈。

```json
{"meta":{"review_id":"sales-model","revision":1,"iteration":1,"title":"销售评审"},
 "brief":{"goal":"比较订单总额","deliverable":"OKF v0.1","scope":"订单","boundary":"不含退款"},
 "constraints":["有证据才批准"],
 "objects":[{"id":"fact/order","kind":"fact","title":"Order",
 "evidence":[{"id":"e1","source":"contract-v1#ListOrders：每行一个已完成订单"}],
 "decisions":[{"id":"grain","question":"Order 一行代表什么？",
 "value":"一个已完成订单","basis":"explicit","confidence":"high","status":"pending",
 "priority":"blocking","impact":"防止重复计数","risk":"错误总额",
 "options":[],"relations":[]}]}]}
```

对象种类为 `fact|dimension|measure|metric|routing`，每个对象拥有证据和决定。
决定含 ID、问题、影响、风险、证据基础、置信度、优先级及建议值或候选，新增决定初始 pending。
明确且高置信可用单值确认；有支持但未定的提案给二至四个互斥候选。
完全缺证据时可无建议值和候选，通过补证或修订范围处理，不编造选择。
候选含 `id,label,when,benefit,cost,risk,reason,evidence,recommended`，
证据引用对象内 ID，且恰有一个有依据的推荐项。

## 关系与反馈

关系为 `{type,target,note}`，目标格式 `<object-id>#<decision-id>`。
`depends_on` 的前提未解决时阻塞，循环、自引用、缺目标属于错误。
`conflicts_with` 表示同时接受两项当前提案无效，双向展示并阻止批准；
若只针对某些候选组合冲突，须拆分或重述问题，明确冲突范围。
`tradeoff_with` 双向展示但只提供信息。前提选择改变后清除依赖项反馈，以便重新考虑。

用户可确认单值、选择候选、修正、补证或拒绝问题。
修正、补证、拒绝进入下一版本，拒绝不隐式删除对象。缺证据决定不能批准。
始终可导出草稿；只有全部决定已解决且无冲突、阻塞或模型错误才可批准导出。
`approved:true` 需要用户主动操作。

## 版本与完成

同一评审保持 `meta.review_id`，提案改变时递增 `revision`。
导出包含 `review_id`、`revision`、`model_fingerprint`；每项 `decisions`
含 `id`、`proposal_fingerprint`、`action`。指纹用于发现误用旧反馈，不是身份认证。
导入检查动作和候选 ID；保留内容匹配的决定，报告已变提案，不恢复旧批准。
依赖、证据或上下文改变同样使相关决定指纹失效。旧无版本反馈须与原始模型核对，不能盲目导入。

修订日志记录日期、决定 ID、新旧值、理由与出处。语义改变后重出模型和报告。
沿用未变的已确认选择，包括聊天中已明确给出的批准；工作台是收集辅助，不是二次必经审批。
确需确认时先完成独立工作，再呈现具体未决选择。输出前核对当前模型、来源与已批准反馈。
验证草稿导出、批准门禁、前提变更、旧反馈导入与往返；不能假定浏览器点击已回传 Agent。
