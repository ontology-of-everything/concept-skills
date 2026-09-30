# software-concept-architect-review-cn QA

Per-skill quality gate. Run `validate.sh` locally and in CI via
`tools/validate-all.sh`.

## Layout

```text
qa/software-concept-architect-review-cn/
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
./qa/software-concept-architect-review-cn/validate.sh
```

共享规格的维护源为 `skills/software-concept-architect-design/references/spec-format.md`。修改后运行 `rtk python3 tools/sync-concept-contract.py --write` 分发给其他 concept 包；各 validate.sh 自动检查一致性。副本用于独立安装，避免依赖伴生技能。行为 eval 用于场景推演，不由静态门禁代跑。
