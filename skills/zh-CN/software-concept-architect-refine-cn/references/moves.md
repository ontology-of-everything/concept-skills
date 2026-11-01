# 设计手法

按实际场景选手法，不凭规模、名称或共享字段判断。

| 手法 | 决定与权衡 |
| --- | --- |
| 拆分/合并 | 分离职责或组合不同概念，权衡简单性、控制与能力。 |
| 统一/特化 | 合并变体或保留专门行为，权衡通用性与实际需要。 |
| 收紧/放松 | 增加或放松同步，权衡自动化与用户控制。 |

过窄只有排除所需行为时才构成问题，特化可以合理。范围由根因决定，不按改动行数判断。
保留不改选项，沿用授权。只读审查交付建议，不改文件。

选定改动须说明证据、备选、行为差异、契约/规则影响与检查。保持不变量，验证应用需要。
区分设计推演与实测，也区分有意重新设计与保持行为的重构。

## 来源

- Daniel Jackson，[Design Moves for Software](https://essenceofsoftware.com/posts/design-moves/)，2022-04-18。手法与权衡。
- Daniel Jackson，[Beyond Objects](https://arxiv.org/abs/2606.27258)，2026-06-25。按对象分功能导致的混杂与碎片化。
- Eagon Meng 等，[Making Software Meaningful](https://arxiv.org/abs/2606.11051)，2026-06-09。以可观察行为建立共享含义。
- [What You See Is What It Does](https://arxiv.org/abs/2508.14511)，2025。独立概念与显式同步。

流程改编自上述文献，日期标识所参考版本。
