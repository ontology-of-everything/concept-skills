# 图示设计规范

Rank、Role、Relation、Rule 共用本文件。图的含义与结构放在各 R 的参考中，主题参数在这里维护。

## 表达与布局

- 图前说明视角、边界和 Rank。节点用短名称，第二行可放职责或技术说明。
- 子图表示归属或边界。连线标注方向和交换内容，分别说明调用、源码依赖和数据流。
- 运行交互图用实线表示请求或数据访问，虚线表示异步通知。其他图法另行说明边的含义。时序图用 `->>` 调用、`-->>` 返回、`-)` 异步消息。
- 每图回答一个主要问题。拥挤时按层级或场景拆图，减少交叉线和长标签。

## 颜色与描线

| 语义类 | 用途 | 暗色强调色 | 亮色强调色 |
|---|---|---|---|
| `entry` | 前端与入口 | `#22D3EE` | `#0E7490` |
| `service` | 业务服务 | `#34D399` | `#047857` |
| `worker` | 后台任务 | `#2DD4BF` | `#0F766E` |
| `data` | 数据存储 | `#C084FC` | `#7E22CE` |
| `security` | 安全与身份 | `#FB7185` | `#BE123C` |
| `message` | 消息设施 | `#F59E0B` | `#B45309` |
| `infra` | 云与网络设施 | `#FACC15` | `#A16207` |
| `external` | 外部系统 | 中性灰 | 中性灰 |

节点描边 1.2px、圆角 8px。分组描边 1px、圆角 10px、虚线 `4 3`。分组使用 `boundaryService`、`boundaryWorker`、`boundaryData` 或 `boundaryInfra`，含义与对应节点类一致。

暗色画布用 `#07111F`，亮色用 `#F8FAFC`。名称加粗，说明用次级文字色。图标可用单色线形符号，不依赖远程资源。低对比网格由展示容器提供，普通文档使用纯色背景。

## 应用主题

选择一套主题。把 YAML 配置放在 Mermaid 代码块开头的 `---` 分隔符之间，再接各类图模板。结构图还需在末尾加入同主题的 `classDef` 样式声明，保留模板中的语义类。时序图和状态图只用 YAML 配置。

暗色与亮色只改变样式。切换时保留角色、关系、名称和布局。导出 PNG 时设置对应画布色，透明 SVG 可放在主题画布上。

### 暗色

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

### 亮色

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

## 检查

检查明暗版语义是否一致，正文和次级文字对比度是否足够，标题、箭头、边界是否清楚。分别检查原尺寸与文档宽度下的渲染。
