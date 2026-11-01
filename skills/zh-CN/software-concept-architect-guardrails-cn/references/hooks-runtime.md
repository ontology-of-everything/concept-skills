# 可选 hooks 运行时

只在用户要求时启用，需要 Claude Code、bash 和 jq。保留 wyx v0.26.0 脚本与 MIT 通知，规格工作本身不依赖 hooks。

| Hook | 行为 |
| --- | --- |
| SessionStart | 列规格、历史最后快照、mtime 线索、遮蔽提示与缺 jq 警告。 |
| PreToolUse | Write/Edit/NotebookEdit 前找最近 CONCEPT/PIPELINE，只注入 PIPELINE data boundary。 |
| PostToolUse | 查旧 CONCEPT dependencies，本记法下静默。 |

最近 CONCEPT/PIPELINE 终止边界查找，SYNCS 只列名。只有 PIPELINE 时可能再查祖先并标 SHADOWED。
根目录依次取 CLAUDE_PROJECT_DIR、输入 cwd、当前目录，空根或文件系统根则停止。
提取器只识别有限标题，跳过 json/jsonl/lock/log/txt，编辑规格时提示校对。

hooks 不阻断写入，不检查 import、契约或规则，也不自动覆盖 Bash/MCP 写入和其他客户端。
须主动读本地规格，不能补旧节迎合提示。

## 启用与检查

先读 runtime/hooks/hooks.json 与三个运行时脚本，保留既有设置：

```bash
claude --plugin-dir /绝对路径/skills/software-concept-architect-guardrails-cn/runtime
```

渠道缺插件清单时，将 runtime/hooks/hooks.json 合并到项目 .claude/settings.json，CLAUDE_PLUGIN_ROOT 替换为绝对路径。
启用前运行 bash -n 并解析 JSON。设 CLAUDE_PROJECT_DIR 后运行 bash runtime/scripts/session-start.sh，开启新会话，确认各 hook 只触发一次且不影响其他工作。
移除时恢复旧设置，只删除本技能安装的文件。

历史仅按明确请求保存，格式见[漂移检测](drift-detection.md#报告与可选历史)。SessionStart 读取最后快照，fix 使用 specs_remaining。
局部扫描与 mtime 不证明全仓新鲜。运行时没有 check-rules.sh，校验在本仓 QA。
