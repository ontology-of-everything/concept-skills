# Phase 3: OKF compatibility output

Default to an OKF v0.1 compatibility bundle to preserve existing consumers. The canonical home is
[GoogleCloudPlatform/open-knowledge-format](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md);
its current specification is v0.2. Record the chosen version; migrate only when requested or required
by the target consumer. Do not mix version-specific provenance fields by accident.

## Format versus this skill's profile

OKF uses Markdown and YAML frontmatter; ordinary concept documents require a nonempty `type`.
Types are extensible. IDs derive from paths without `.md`, not a required `id` key. Root `index.md`
may declare `okf_version`; nested indexes have no frontmatter. Names, body sections, and this skill's
semantic fields are producer conventions, not OKF hard constraints. A knowledge document here
called a "concept" is distinct from a Jackson behavioral concept.

Our profile requires the shared semantics from [YAML mapping](emit-yaml.md), readable titles,
descriptions, claim-level evidence, and resolved in-scope links. Use:

```text
<bundle>/
  index.md
  facts/<fact>.md          # type: Semantic Fact
  dimensions/<dim>.md      # type: Dimension
  metrics/<metric>.md      # type: Metric, when separately useful
  references/<op>.md       # type: API Endpoint or suitable source type
```

These custom types and folders are local defaults. Keep fact-level quantities in their fact
document; a Metric document defines the named calculation and links to its source measures. A source table is not an API Endpoint.
The root index carries `okf_version: "0.1"` and links entry points and objects. Concepts carry
`type`, `title`, `description`, relevant semantic extension fields, and Markdown explanations.
Use a `# Citations` section for v0.1 evidence. For v0.2 output, use its `sources` provenance and
`generated` conventions instead; record actual authorship/verification, never invented trust signals.

Use `/dimensions/store.md` for bundle-root links, or standard relative links. Explain join,
parent, and derivation relationships in prose. An OKF consumer may tolerate unfinished links;
our delivery profile still reports unresolved in-scope references. Keep amendments/approval logs
outside the bundle or in `log.md`; an ordinary `.md` becomes a concept document and needs frontmatter.
A multi-bundle parent index links each bundle once without copying its semantics.
