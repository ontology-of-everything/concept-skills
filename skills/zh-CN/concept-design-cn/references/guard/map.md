# 概念与同步关系图

从本地 CONCEPT 与 SYNCS 生成含 Mermaid 图的 `ARCHITECTURE.md`。
版本 1 不读取 PIPELINE、PRD 或源码。

```sh
python3 <skill-directory>/scripts/concept_map.py <root> --output <root>/ARCHITECTURE.md
```

用 `--scope RELPATH` 选择定义、规则及其直接实例边界。
重复 `--exclude PATTERN` 排除路径。
省略 `--output` 时向 stdout 输出 Markdown。
`--check` 须配合 `--output`，只读比较。

身份、解析与输出规则见[图格式](../map-format.md)。
报告输出路径或 stdout、范围、退出状态与缺口。
局部可解析结果可写入，但 MUST 标为 partial。
无规格时 MUST NOT 清空旧图。
本图映射规格引用，不是 Jackson 的目的依赖图。
它不证明代码覆盖率或运行正确性。
