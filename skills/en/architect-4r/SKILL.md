---
name: architect-4r
description: Use only when explicitly invoked. Model systems with Li Yunhua's 4R method and create separate Mermaid diagrams for Rank, Role, Relation, and Rule, with templates and checks.
metadata:
  language: en
  translation_of: architect-4r-cn
  version: "0.3.0"
  openclaw:
    homepage: https://github.com/ontology-of-everything/concept-skills/tree/main/skills/en/architect-4r
---

# 4R system modeling framework

## Core concepts and definitions

4R is an ontological framework for describing a system. At a defined observation level, roles, relations, and rules form an explicit specification of its structure and behavior.

| Dimension | Definition | Diagram reference |
|---|---|---|
| Rank | The model's observation scope and granularity, determining which objects and details belong at the current level. | [Hierarchy and expansion](references/rank.md) |
| Role | A part at the current level with explicit responsibilities and state ownership. | [Composition and responsibilities](references/role.md) |
| Relation | Calls, dependencies, information transfers, or shared resources between roles, including direction and exchanged content. | [Role relationships](references/relation.md) |
| Rule | The conditions, order, and constraints of collaboration, including state changes and failure handling. | [Sequence, flow, and state](references/rule.md) |

Relation describes static connections. Rule explains when and under what conditions those connections operate.

Business, system, application, and deployment are perspectives. Rank determines the granularity of each view. Systems or services fulfill business capabilities. The application perspective describes internal modules and dependencies. The deployment perspective maps runtime units to infrastructure.

A complete 4R architecture description includes separate diagrams for Rank, Role, Relation, and Rule. A dimension may need several diagrams. Keep names consistent and identify level and object mappings. Apply 4R within each selected perspective.

Use Mermaid for every diagram and the shared [diagram design reference](references/diagram-design.md) for visual parameters. The table links to drawing guidance, templates, and checks for each R.

## Principles

- System boundaries and observation levels determine the meaning of roles and relations.
- An object can be a role at one level and expand into a system of further roles.
- Views describe the same system, with consistent object names and mappings.
- Key scenarios check consistency between structure and collaboration rules.

## Avoiding mistakes

- Perspectives and levels are distinct. The four architecture views do not correspond to fixed L1 through L4 levels.
- Relations do not replace rules. Successful paths do not replace conditions, constraints, or failure rules.
- Technology names and folder structures do not establish responsibility boundaries. Distinguish runtime calls from source dependencies.
- Assign state changes and failure handling to explicit roles.
- Separate current state, target design, and inference. Leave unsupported structures and rules unconfirmed.
