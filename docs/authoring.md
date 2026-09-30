# Skill authoring

Conventions for skills in this monorepo. Spec baseline: [agentskills.io](https://agentskills.io/specification).

## Layout

| Path | Purpose |
| --- | --- |
| `skills/en/<name>/` | English install payload (`SKILL.md` plus optional resources) |
| `skills/cn/<name>-cn/` | Simplified-Chinese install payload |
| `qa/<locale>/<name>/` | Validation, evals, assertions; never installed |
| `docs/skills/<locale>/<name>.md` | Human-facing skill overview |

Every capability ships as an English/default and `-cn` pair. Follow [localization.md](localization.md).

QA layout (gate files stay under `qa/`, not `skills/`):

```text
qa/<locale>/<name>/
├── validate.sh
├── skillcheck.toml
├── .markdownlint.json
├── policy.skill-scanner.yaml   # optional
├── README.md
├── evals/evals.json
├── evals/llm-rubric.yml
├── assertions/README.md
├── fixtures/
└── bin/
    ├── gate.py                 # optional: gate.py style (skillcheck + markdownlint + skill-scanner)
    └── …
```

## Naming

- Folder name = `name` in `SKILL.md` frontmatter (kebab-case, lowercase)
- English paths only under `skills/` and `references/`
- Flat `references/*.md`; entity YAML under `references/semantic/` when needed

## SKILL.md frontmatter

Required: `name`, `description` (trigger keywords + scope).

Recommended for marketplace discovery ([SkillsMP](https://skillsmp.com/), [skills.sh](https://www.skills.sh/), [ClawHub](https://clawhub.ai/)):

```yaml
compatibility: <bins, IAM, network; note if agent must not auto-install>
metadata:
  openclaw:          # ClawHub security review only
    requires:
      bins: [<cli>]
    homepage: https://github.com/<org>/<repo>/tree/main/skills/<name>
    envVars:         # optional; required: false for profile-based auth
      - name: EXAMPLE_API_KEY
        required: false
        description: ...
```

- **`description`**: English + Chinese trigger phrases, task scope, and explicit refuse rules (payment/delete/refund).
- **License**: keep the repository license at the repo root. Do not put a
  conflicting `license` field in installable skill frontmatter when targeting
  ClawHub, because ClawHub-published skills are MIT-0.
- **SkillsMP**: public GitHub repo with `SKILL.md` frontmatter. Keep GitHub
  topics `claude-skills` and `claude-code-skill` on the monorepo; indexing is
  crawler-driven (no submit API)—recheck search after push.
- **skills.sh**: listing is telemetry from `npx skills add <org>/concept-skills`
  (no submit API). Promote that install in README; optional badge
  `https://skills.sh/b/<org>/concept-skills`. Group the repo page with root
  [`skills.sh.json`](../skills.sh.json) (display-only; does not change the CLI).
- **ClawHub**: publish from `skills/<name>/` with `clawhub skill publish`.
  Declare `metadata.openclaw` so scans match runtime behavior.
  Publish with the catalog `display_title` as `--name`; use `display_name` for the Agent UI.
  The current CLI skips dot directories, including the Guardrails runtime plugin manifest.
  For that bundle, include `runtime/.claude-plugin/plugin.json` through the official upload/publish
  API and verify the complete remote file list and hashes before withdrawing old versions.

Keep frontmatter concise; put long guidance in `references/`.

## Classification and ClawHub publishing

`docs/catalog.yml` is the source of truth for discovery metadata:

- `domains` defines the repository taxonomy; each localized skill has one `domain`.
- `subdomains` describes internal specializations. Each English entry's `clawhub.categories`
  maps to ClawHub's controlled browse categories; `clawhub.topics` holds up to five specific topics.
- Chinese editions share their English counterpart's domain and are not published to ClawHub.
- `clawhub.enabled: false` defers a listing; its reason explains the blocker.
- `clawhub.slug` records an approved marketplace URL slug when it differs from the local skill name.

Run `python3 tools/skill-catalog.py --write` after catalog edits to regenerate the README skill
sections and `skills.sh.json`. `tools/validate-all.sh` detects stale generated views, invalid
categories/topics, mismatched localized domains, and accidental Chinese publication targets.

For an existing listing, use **ClawHub Settings → Catalog metadata** to change only categories
and topics without creating a new version. Record the same values in the catalog first.

For a new content release, update the paired QA/catalog versions and changelogs, then preview:

```bash
python3 tools/publish-clawhub.py data-knowledge-architect
```

Add `--publish --notes-file /absolute/path/release-notes.txt` to submit the reviewed release.
The publisher reads the catalog title, version, categories, and topics, verifies the remote skill
identity, runs QA, and uploads the complete bundle through ClawHub's official API. It includes
hidden runtime manifests such as Guardrails' `runtime/.claude-plugin/plugin.json`, which the
current CLI skips. Credentials stay in the existing ClawHub CLI login.

A pending submission is not a completed publication. Verify the public version, title,
categories/topics, and complete file hashes before announcing completion. Existing version
numbers and unexpected slug redirects stop publishing instead of overwriting another skill.

## Codex UI metadata (`agents/openai.yaml`)

Optional per-skill file read by the harness, not the agent
([Codex skills docs](https://developers.openai.com/codex/skills)). Present in the
`software-concept-architect-*` and `software-concept-architect-guardrails` bundles:

```yaml
interface:
  display_name: "Software Concept Architect · Design"   # required when the file exists
  short_description: "..."                 # required, 25–64 chars
  default_prompt: "Use $software-concept-architect-design to ..."   # must name the skill as $name
```

Add `policy.allow_implicit_invocation: false` only when a skill should stay out of automatic
selection and be invoked as `$name`. Keep values consistent with `SKILL.md`; regenerate when the
description changes.

## Interaction discipline (all skills)

One **Agent discipline** / **工作准则** bullet per `SKILL.md` (template default). Canonical line unless the domain is stricter:

> 歧义仅问改查证路径者；已述/已决不重问；可自证则推进；须裁断则一次一问。

| Do | Don't |
| --- | --- |
| One blocking ask when scope, time, money basis, or ID changes routing | Re-ask settled scope, cycle, or read-only intent |
| Route and deliver when facts suffice | Multi-item clarification before any investigation |
| Layer domain mandatory clarifiers (`evidence_boundary`, partner `customer_id`) | Skip evidence boundaries because “don't ask” |

Evals: `proceed-without-reasking-*`, `single-clarification-*` in `qa/<name>/evals/evals.json`. Offline: `protocol_grading.py`; LLM: `interaction_discipline` in `llm-rubric.yml`.

## Install purity

Do **not** place inside `skills/<name>/`:

- `evals/`, `tests/`, `qa/`
- `.workspaces/`, `analysis/`
- repo-level scripts or credentials

## Validation

Per skill:

```bash
./qa/<name>/validate.sh
```

All skills:

```bash
./tools/validate-all.sh
```

New skill scaffold:

```bash
./tools/skill-scaffold.sh <skill-name>
```

## Skill Creator eval loop

```text
qa/<name>/evals/evals.json
        │
        ├── with_skill ──► <name>-workspace/iteration-N/eval-<id>/with_skill/
        └── baseline   ──► .../without_skill/
```

`<name>-workspace/` at repo root is gitignored; do not commit it.

Register the skill in `docs/catalog.yml` when adding a new package.
