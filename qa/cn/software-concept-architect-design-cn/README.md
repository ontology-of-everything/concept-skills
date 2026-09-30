# software-concept-architect-design-cn QA

Per-skill quality gate. Run `validate.sh` locally and in CI via
`tools/validate-all.sh`.

## Layout

```text
qa/software-concept-architect-design-cn/
├── validate.sh              # entry point (required)
├── README.md
├── evals/evals.json         # Skill Creator eval cases
├── assertions/README.md     # assertion rubric for eval authors
├── fixtures/                # optional: contract YAML, golden files
└── bin/                     # optional: helper scripts
```

Add `fixtures/` and `bin/` when the skill needs cross-layer checks beyond
`skills-ref`, markdownlint, and skillcheck.

## Commands

```bash
./qa/software-concept-architect-design-cn/validate.sh
```

## Token 复核

`token-baseline.json` 保存本次任务开始时工作树（包含已有未提交修改）的各文件 token 数与 SHA-256；不是 HEAD 基线。
使用 o200k_base，复核命令：

```bash
uv run --with tiktoken python qa/software-concept-architect-design-cn/measure-tokens.py
```

分别报告入口、全部 Markdown 和包含原样 runtime 的全部载荷；文件搬到 references 不算总量压缩。基线记录 tokenizer 版本；新 runtime/参考文件也纳入当前统计。

共享规格的维护源为 `skills/software-concept-architect-design-cn/references/spec-format.md`。修改后运行 `rtk python3 tools/sync-concept-contract.py --write` 分发给其他 concept 包；各 validate.sh 自动检查一致性。副本用于独立安装，避免依赖伴生技能。行为 eval 用于场景推演，不由静态门禁代跑。
