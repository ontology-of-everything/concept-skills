# software-concept-architect-guardrails-cn QA

Per-skill quality gate. Run `validate.sh` locally and in CI via
`tools/validate-all.sh`.

## Layout

```text
qa/software-concept-architect-guardrails-cn/
├── validate.sh              # entry point (required)
├── README.md
├── VERSION
├── CHANGELOG.md
├── .markdownlint.json
├── evals/evals.json         # Skill Creator eval cases
└── assertions/README.md     # assertion rubric for eval authors
```

## Checks beyond the shared template

- **References routing** — each of the seven `references/*.md` files exists and is
  reachable from `SKILL.md`'s mode table. A mode that routes nowhere is a dead mode.
  The six bare mode names (`audit`, `concept`, `drift`, `pipeline`, `sync`, `map`)
  must appear in the table, and the pre-0.30.0 `wyx:` prefix must not reappear in
  `SKILL.md` or `references/`.
- **Runtime integrity** — the three upstream hook scripts parse under `bash -n`,
  `hooks.json` still registers SessionStart / PreToolUse / PostToolUse, both JSON
  files are parseable, and the upstream MIT notice is present. The runtime is
  vendored verbatim, so this gate catches an accidental edit rather than a bug.

## Commands

```bash
./qa/software-concept-architect-guardrails-cn/validate.sh
```

共享规格的维护源为 `skills/software-concept-architect-design/references/spec-format.md`。修改后运行 `rtk python3 tools/sync-concept-contract.py --write` 分发给其他 concept 包；各 validate.sh 自动检查一致性。副本用于独立安装，避免依赖伴生技能。行为 eval 用于场景推演，不由静态门禁代跑。
