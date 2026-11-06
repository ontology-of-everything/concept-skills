# Diagram design

Rank, Role, Relation, and Rule share this file. Their references define meaning and structure. Maintain theme parameters here.

## Expression and layout

- State perspective, boundary, and Rank before the diagram. Use short node names and an optional second line for responsibility or technology.
- Use subgraphs for ownership or boundaries. Label direction and exchanged information. Distinguish calls, source dependencies, and data flows.
- Runtime interaction views use solid lines for requests or data access and dashed lines for asynchronous notifications. Other diagram types state their edge meanings separately. Sequence views use `->>` for calls, `-->>` for returns, and `-)` for asynchronous messages.
- Let each diagram answer one main question. Split crowded views by level or scenario and reduce crossing lines and long labels.

## Colors and strokes

| Semantic class | Purpose | Dark accent | Light accent |
|---|---|---|---|
| `entry` | Frontend and ingress | `#22D3EE` | `#0E7490` |
| `service` | Business services | `#34D399` | `#047857` |
| `worker` | Background jobs | `#2DD4BF` | `#0F766E` |
| `data` | Data storage | `#C084FC` | `#7E22CE` |
| `security` | Security and identity | `#FB7185` | `#BE123C` |
| `message` | Messaging | `#F59E0B` | `#B45309` |
| `infra` | Cloud and networking | `#FACC15` | `#A16207` |
| `external` | External systems | Neutral gray | Neutral gray |

Use 1.2px strokes and 8px corners for nodes. Use 1px strokes, 10px corners, and a `4 3` dash pattern for groups. Group classes are `boundaryService`, `boundaryWorker`, `boundaryData`, and `boundaryInfra`, with the same meanings as their node classes.

Use canvas `#07111F` for dark and `#F8FAFC` for light. Make names bold and use secondary text color for details. Optional icons use monochrome line symbols without remote resources. The display container provides a low-contrast grid. Ordinary documents use a solid background.

## Applying a theme

Choose one theme. Put its YAML configuration between `---` delimiters at the start of the Mermaid code block, then append a type's template. For structure views, also append that theme's `classDef` declarations and retain the template's semantic classes. Sequence and state views use only the YAML configuration.

Switching themes changes style only. Preserve roles, relations, names, and layout. Set the canvas color when exporting PNG. Place transparent SVGs on a matching theme canvas.

### Dark

```yaml
config:
  theme: "base"
  look: "classic"
  fontFamily: "\"PingFang SC\", \"Helvetica Neue\", Arial, sans-serif"
  flowchart: {nodeSpacing: 28, rankSpacing: 40, padding: 14, curve: basis}
  sequence: {mirrorActors: false, actorMargin: 42, messageMargin: 28, boxMargin: 10}
  themeVariables: {darkMode: true, background: '#07111F', fontFamily: '"PingFang SC", "Helvetica Neue", Arial, sans-serif', fontSize: 15px,
      primaryColor: '#0B2B25', primaryTextColor: '#E6EDF3', primaryBorderColor: '#34D399', lineColor: '#B8C4D4',
      textColor: '#E6EDF3', secondaryColor: '#211532', tertiaryColor: '#101B2B', clusterBkg: '#101B2B', clusterBorder: '#66758A',
      edgeLabelBackground: '#07111F', actorBkg: '#101B2B', actorBorder: '#34D399', actorTextColor: '#E6EDF3', actorLineColor: '#66758A',
      signalColor: '#B8C4D4', signalTextColor: '#E6EDF3', labelBoxBkgColor: '#101B2B', labelBoxBorderColor: '#66758A',
      labelTextColor: '#E6EDF3', loopTextColor: '#E6EDF3', noteBkgColor: '#28220E', noteBorderColor: '#FACC15',
      noteTextColor: '#E6EDF3', activationBkgColor: '#0B2B25', activationBorderColor: '#34D399', sequenceNumberColor: '#07111F'}
  themeCSS: |
    .nodeLabel small { color: #9AA9BC; font-size: 12px; }
    .nodeLabel b { font-weight: 600; }
    .cluster-label { font-weight: 600; }
    .edgeLabel { background-color: #07111F; color: #9AA9BC; }
    .cluster rect { rx: 10; ry: 10; }
    .actor { rx: 8; ry: 8; }
```

```text
classDef entry fill:#082A36,stroke:#22D3EE,color:#E6EDF3,stroke-width:1.2px,rx:8,ry:8
classDef service fill:#0B2B25,stroke:#34D399,color:#E6EDF3,stroke-width:1.2px,rx:8,ry:8
classDef worker fill:#0B292B,stroke:#2DD4BF,color:#E6EDF3,stroke-width:1.2px,rx:8,ry:8
classDef data fill:#211532,stroke:#C084FC,color:#E6EDF3,stroke-width:1.2px,rx:8,ry:8
classDef security fill:#301B26,stroke:#FB7185,color:#E6EDF3,stroke-width:1.2px,rx:8,ry:8
classDef message fill:#30230F,stroke:#F59E0B,color:#E6EDF3,stroke-width:1.2px,rx:8,ry:8
classDef infra fill:#2A260F,stroke:#FACC15,color:#E6EDF3,stroke-width:1.2px,rx:8,ry:8
classDef external fill:#101B2B,stroke:#66758A,color:#E6EDF3,stroke-width:1.2px,rx:8,ry:8
classDef boundaryService fill:#081821,stroke:#34D399,color:#34D399,stroke-width:1px,stroke-dasharray:4 3,rx:10,ry:10
classDef boundaryWorker fill:#081822,stroke:#2DD4BF,color:#2DD4BF,stroke-width:1px,stroke-dasharray:4 3,rx:10,ry:10
classDef boundaryData fill:#0E1224,stroke:#C084FC,color:#C084FC,stroke-width:1px,stroke-dasharray:4 3,rx:10,ry:10
classDef boundaryInfra fill:#11171B,stroke:#FACC15,color:#FACC15,stroke-width:1px,stroke-dasharray:4 3,rx:10,ry:10
```

### Light

```yaml
config:
  theme: "base"
  look: "classic"
  fontFamily: "\"PingFang SC\", \"Helvetica Neue\", Arial, sans-serif"
  flowchart: {nodeSpacing: 28, rankSpacing: 40, padding: 14, curve: basis}
  sequence: {mirrorActors: false, actorMargin: 42, messageMargin: 28, boxMargin: 10}
  themeVariables: {darkMode: false, background: '#F8FAFC', fontFamily: '"PingFang SC", "Helvetica Neue", Arial, sans-serif',
      fontSize: 15px, primaryColor: '#ECFDF5', primaryTextColor: '#142238', primaryBorderColor: '#047857', lineColor: '#52657D',
      textColor: '#142238', secondaryColor: '#FAF5FF', tertiaryColor: '#F1F5F9', clusterBkg: '#F1F5F9', clusterBorder: '#8090A4',
      edgeLabelBackground: '#F8FAFC', actorBkg: '#F1F5F9', actorBorder: '#047857', actorTextColor: '#142238', actorLineColor: '#8090A4',
      signalColor: '#52657D', signalTextColor: '#142238', labelBoxBkgColor: '#F1F5F9', labelBoxBorderColor: '#8090A4',
      labelTextColor: '#142238', loopTextColor: '#142238', noteBkgColor: '#FFFBEB', noteBorderColor: '#92400E',
      noteTextColor: '#142238', activationBkgColor: '#ECFDF5', activationBorderColor: '#047857', sequenceNumberColor: '#F8FAFC'}
  themeCSS: |
    .nodeLabel small { color: #53647A; font-size: 12px; }
    .nodeLabel b { font-weight: 600; }
    .cluster-label { font-weight: 600; }
    .edgeLabel { background-color: #F8FAFC; color: #53647A; }
    .cluster rect { rx: 10; ry: 10; }
    .actor { rx: 8; ry: 8; }
```

```text
classDef entry fill:#ECFEFF,stroke:#0E7490,color:#142238,stroke-width:1.2px,rx:8,ry:8
classDef service fill:#ECFDF5,stroke:#047857,color:#142238,stroke-width:1.2px,rx:8,ry:8
classDef worker fill:#F0FDFA,stroke:#0F766E,color:#142238,stroke-width:1.2px,rx:8,ry:8
classDef data fill:#FAF5FF,stroke:#7E22CE,color:#142238,stroke-width:1.2px,rx:8,ry:8
classDef security fill:#FFF1F2,stroke:#BE123C,color:#142238,stroke-width:1.2px,rx:8,ry:8
classDef message fill:#FFF7ED,stroke:#B45309,color:#142238,stroke-width:1.2px,rx:8,ry:8
classDef infra fill:#FFFBEB,stroke:#A16207,color:#142238,stroke-width:1.2px,rx:8,ry:8
classDef external fill:#F1F5F9,stroke:#8090A4,color:#142238,stroke-width:1.2px,rx:8,ry:8
classDef boundaryService fill:#F5FBFA,stroke:#047857,color:#047857,stroke-width:1px,stroke-dasharray:4 3,rx:10,ry:10
classDef boundaryWorker fill:#F6FBFB,stroke:#0F766E,color:#0F766E,stroke-width:1px,stroke-dasharray:4 3,rx:10,ry:10
classDef boundaryData fill:#F9F9FD,stroke:#7E22CE,color:#7E22CE,stroke-width:1px,stroke-dasharray:4 3,rx:10,ry:10
classDef boundaryInfra fill:#FAFAF7,stroke:#A16207,color:#A16207,stroke-width:1px,stroke-dasharray:4 3,rx:10,ry:10
```

## Checks

Check that themes preserve meaning, text and secondary labels have enough contrast, and titles, arrows, and boundaries remain clear. Inspect rendering at native size and document width.
