# concept-skills

Ontology, semantic-layer, and concept-design skills monorepo.

## Do not get wrong

- **`skills/<name>/` = install payload only** (`npx skills add` copies this tree). Put gates, evals, and `skillcheck.toml` under **`qa/<name>/`** (`validate.sh` → `bin/gate.py full`); never inside `skills/`.
- **Skill Creator eval output:** `<name>-workspace/` at **repo root only** (gitignored). Never under `skills/` — `npx skills add` would ship it. Run evals from repo root so paths resolve to `./<name>-workspace/`.
- **Do not edit or commit:** `.agents/`, `*-workspace/`, `.workspaces/`, `.credentials/`, gate reports.
- **Done means** `./qa/<name>/validate.sh` (or `./tools/validate-all.sh`) passes — say so only after running it.
- **Skill change** syncs five places: `skills/`, `qa/` (`VERSION`, `CHANGELOG.md`), `docs/catalog.yml`, `docs/skills/<name>.md`. New skill: `./tools/skill-scaffold.sh <name>`.
- **Localization**: English lives at `skills/en/<name>`; Simplified Chinese at `skills/cn/<name>-cn`. Update each pair together and follow `docs/localization.md`; `tools/validate-localization.py` is the parity gate.
- **ClawHub**: publish only `skills/en`; never sync `skills/cn` to ClawHub.
- **No commit** unless asked. Never commit `.env*`, AK/SK, or credential files. Minimal diffs; no extra markdown unless asked.
