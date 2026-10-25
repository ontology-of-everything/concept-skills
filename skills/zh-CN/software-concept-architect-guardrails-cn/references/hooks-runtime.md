# 可选 hooks 运行时

焦点：哪些规格信息会被自动提示？runtime 保留 wyx v0.26.0 脚本/hooks 和 MIT 通知，插件清单已改名。规格工作不依赖 Claude Code；自动注入需 Claude Code、bash/jq。

## 能力与限制

| hook | 本仓 Jackson 记法下的行为 |
| --- | --- |
| SessionStart | 列规格、覆盖线索、历史最后结果、mtime 提示和遮蔽告警；缺 jq 则警告 |
| PreToolUse | Write/Edit/NotebookEdit 前向上找最近 CONCEPT/PIPELINE；只注入 PIPELINE data boundary，CONCEPT 提示无旧边界段 |
| PostToolUse | 查 CONCEPT dependencies；本记法没有此节，因而静默 |

最近含 CONCEPT/PIPELINE 的目录终止边界查找，SYNCS 只列名；仅有 PIPELINE 时再找祖先 CONCEPT，可能标 SHADOWED。主动读本地规格及相关 sync，祖先提示不能替代它；避免根级 CONCEPT 笼罩无关模块。

项目根依次取 CLAUDE_PROJECT_DIR、输入 cwd、当前目录；根为空或 `/` 则退出，不越界。跳过 json/jsonl/lock/log/txt，编辑规格只给校对提示；提取器支持有限大小写形式，非通用 Markdown 解析器。

核心命题：hook 提示不证明边界成立。它不阻断写入、不解析 import/四节/sync；Bash/MCP 写入及其他客户端不自动受它覆盖。语义核对依靠读规格、架构测试和漂移审查，不能补旧节来迎合提示。

## 启用与自检

用户要求启用时：

```bash
claude --plugin-dir /绝对路径/skills/software-concept-architect-guardrails-cn/runtime
```

渠道缺隐藏插件清单时，将 runtime/hooks/hooks.json 合并到项目 `.claude/settings.json`，替换 CLAUDE_PLUGIN_ROOT 为绝对路径并保留现有设置。自检设 CLAUDE_PROJECT_DIR 后运行 `bash runtime/scripts/session-start.sh`；本仓 QA 在 qa，runtime 无 check-rules.sh。

SessionStart 只读历史最后一条，fix 用 specs_remaining；局部扫描不表示全仓清洁，mtime 不证明语义新鲜。回填提示不改变已确认新行为规格先行的约定。历史仅按明确请求保存真实测量，格式见 [drift-detection.md](drift-detection.md#可选历史)。
