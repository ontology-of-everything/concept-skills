# Phase 3：OKF 兼容输出

默认保留 OKF v0.1 兼容 bundle，以支持已有消费者。规范现位于
[GoogleCloudPlatform/open-knowledge-format](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md)，
当前规范为 v0.2。记录所选版本；仅在用户要求或目标消费者需要时迁移，避免误混版本专属的来源字段。

## 格式与本技能配置

OKF 使用 Markdown 和 YAML frontmatter，普通概念文档要求非空 `type`，类型可扩展。
ID 来自去掉 `.md` 的路径，不是必填 `id` 键。根 `index.md` 可声明 `okf_version`，
子索引不带 frontmatter。名称、正文段落和本技能语义字段属于生产者约定，不是 OKF 硬约束。
这里的知识"concept"文档不同于 Jackson 行为概念。

本技能配置要求[YAML 映射](emit-yaml.md)中的共享语义、可读标题、描述、逐项证据与范围内可解析链接：

```text
<bundle>/
  index.md
  facts/<fact>.md          # type: Semantic Fact
  dimensions/<dim>.md      # type: Dimension
  metrics/<metric>.md      # 独立有用时 type: Metric
  references/<op>.md       # type: API Endpoint 或适合的来源类型
```

自定义类型与目录是本地默认。事实层数量保留在事实文档；Metric 文档定义具名指标并链接来源度量。来源表不应标成 API Endpoint。
根索引带 `okf_version: "0.1"` 并链接入口和对象；概念带 `type`、`title`、`description`、
相关语义扩展字段及 Markdown 说明。v0.1 用 `# Citations` 表达证据；
v0.2 输出改用其 `sources` 来源与 `generated` 约定，记录实际作者与核验，不能编造信任信号。

bundle 根链接可用 `/dimensions/store.md`，也可用标准相对链接。
在正文说明连接、父关系与推导含义。OKF 消费者可容忍未完成链接，本技能交付仍须报告范围内未解析引用。
修订/审批日志放 bundle 外或 `log.md`；普通 `.md` 会被视为概念文档，须有 frontmatter。
多 bundle 父索引每个 bundle 只链接一次，不复制语义。
