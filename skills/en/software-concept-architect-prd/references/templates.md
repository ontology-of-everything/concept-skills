# File Layout for CONCEPT and SYNCS

Read `spec-format.md` first; this file governs where a confirmed model is persisted, not its syntax.
See `example-reserving.md` for a traced example.

| Content                                          | Authoritative location                                                              | Requirement                                                                                                            |
| ------------------------------------------------ | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Application purpose, scenarios, misfits          | overall PRD                                                                         | preserve concept/sync basis and cross-concept assumptions; mark missing purpose open                                   |
| One concept                                      | CONCEPT.md beside its module; stage under `docs/prd/concepts/` before modules exist | transcribe four core sections, declared queries, and notes; concrete types belong in SYNCS                             |
| Application composition                          | SYNCS.md in sync package; stage at `docs/prd/SYNCS.md`                              | one file during transcription, with app/include and rules grouped by `// flow:`; source every external entry signature |
| Acceptance                                       | overall PRD table or existing acceptance file                                       | link every case to an OP, action case, invariant, or application scenario                                              |
| Graphs, dependencies, exclusions, open decisions | overall PRD                                                                         | derive sync graph from rules; give product dependencies independent requirement evidence                               |

Specifications may omit irrelevant details but not confirmed signatures, results, or state meanings.
Resolve every referenced action, query, and type. An absent concept type parameter needs no `[]`; an
action with no returned fields writes `=> []`.

Minimally update existing files and preserve notes and human-authored content. Read legacy dialects
compatibly. A full migration must recover success/error discrimination, correlation, and state
effects rather than converting ambiguity into requirements. When implementation moves staged files
or splits SYNCS by responsibility, update indexes while retaining one authoritative home per
element.
