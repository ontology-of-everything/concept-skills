# Relations and record shape

Use stable ASCII IDs and YAML mappings with `id`, `define`, `sources`, optional `aliases`,
`status: draft|complete`, and optional `updated_at`. Sources are mappings such as
`{source: "notes.md", locator: "section 2", version: "2026-10-01"}`. Record a gap as
`{field: "output", reason: "not specified", source: "notes.md#section-2"}` in `gaps`.
A complete concept adds `applicability` and either `ipo: {inputs, process, outputs}` or
`decomposition` entries with `stage`, `uses`, and `reason`. A scene adds `trigger`, `goal`, and
`stages`; an entity adds `kind` and `role`. List source-supported limits in `constraints`.

Relations use `{type, target, basis: source|synthesis, source, note}`; a scene-stage relation also
names `stage`. Keep different predicates when each adds useful meaning; do not choose an
undefined "strongest" relation. Avoid duplicate edges with identical meaning.

| Type | Direction | Meaning |
| --- | --- | --- |
| contains | concept → concept; entity → entity | Whole/part, not execution order |
| depends-on | concept → concept | The stated method cannot execute without the target under its conditions |
| references | concept → concept | Useful reference without execution dependency |
| invokes | scene/concept → concept/entity | A method or resource used during execution |
| decomposes-to | concept → concept | A meaningful procedural stage |
| parent-child | entity → entity | Source-supported taxonomy/ownership hierarchy; state which |
| assembles | scene stage → concept/entity | A particular stage's orchestration |
| alias | element → alias string | An alternative name, not another record |

There is no minimum edge count or fixed hierarchy depth. Detect contains/decomposition/hierarchy
cycles; report them unless the source explicitly defines a non-hierarchical relation instead.
A mutual execution dependency needs an explained joint procedure or a modeling gap. Preserve
source disagreement rather than merging incompatible methods.

```yaml
- id: method/compare-options
  define: Compare alternatives against explicit decision criteria.
  status: draft
  sources: [{source: notes.md, locator: "section 2"}]
  applicability: null
  gaps: [{field: applicability, reason: "not stated in the source"}]
  relations: []
```

This illustrative record may remain isolated and draft. It is not a requirement that every source
contains this method. Parse each output as YAML and resolve targets across all three files.
