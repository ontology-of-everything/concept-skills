# 关系与记录结构

使用稳定 ASCII ID。YAML 记录包含 `id`、`define`、`sources`，可加 `aliases`、
`status: draft|complete` 与 `updated_at`。出处写为
`{source: "notes.md", locator: "section 2", version: "2026-10-01"}`。
在 `gaps` 中记录缺口，例如 `{field: "output", reason: "原文未说明", source: "notes.md#section-2"}`。
完整概念补 `applicability`，并具备 `ipo: {inputs, process, outputs}`，或含
`stage`、`uses`、`reason` 的 `decomposition`。场景补 `trigger`、`goal`、`stages`；
实体补 `kind`、`role`。在 `constraints` 记录原文支持的局限。

关系写为 `{type, target, basis: source|synthesis, source, note}`；场景阶段关系另标 `stage`。
不同谓词各自有用时可以并存，不选择没有定义的"最强关系"；相同含义的重复边合并。

| 类型 | 方向 | 含义 |
| --- | --- | --- |
| contains | 概念→概念；实体→实体 | 整体与部分，不代表执行顺序 |
| depends-on | 概念→概念 | 在所述条件下，离开目标就无法执行该方法 |
| references | 概念→概念 | 有参考价值，但执行不依赖目标 |
| invokes | 场景/概念→概念/实体 | 执行时使用的方法或资源 |
| decomposes-to | 概念→概念 | 有意义的过程阶段 |
| parent-child | 实体→实体 | 原文支持的分类或所有权层级，须说明是哪种 |
| assembles | 场景阶段→概念/实体 | 特定阶段的编排 |
| alias | 知识元→别名字符串 | 同一对象的其他名称，不是另一条记录 |

不规定最少关系数或固定层级深度。检测包含、分解和层级中的环；除非原文实际定义的是
非层级关系，否则报告问题。相互执行依赖须解释联合过程，或记为建模缺口。
保留来源分歧，不合并不兼容方法。

```yaml
- id: method/compare-options
  define: 根据明确的决策准则比较候选方案。
  status: draft
  sources: [{source: notes.md, locator: "section 2"}]
  applicability: null
  gaps: [{field: applicability, reason: "原文未说明"}]
  relations: []
```

这是允许保持孤立与草稿状态的示意记录，不要求每份原文都包含该方法。
将输出解析为 YAML，跨三个文件解析关系目标。
