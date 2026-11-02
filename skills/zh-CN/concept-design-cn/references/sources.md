# 来源与本地约定

| 依据 | 用途 |
| --- | --- |
| [Jackson，Towards a Theory of Conceptual Design for Software（2015），第8—9节](https://groups.csail.mit.edu/sdg/pubs/2015/concept-essay.pdf) | 目的、运作原理，以及目的论证与实现符合性的区别 |
| [The Essence of Software：资格判据](https://essenceofsoftware.com/tutorials/concept-basics/criteria/) | 软件概念的八项判据 |
| Meng 与 Jackson（MIT），WYSIWID v1，第4—6节（arXiv:2508.14511v1） | 具名输入输出、因果同步、公开状态查询、flow 与触发一致性 |
| [Beyond Objects v1，第12—13节](https://arxiv.org/html/2606.27258v1#S12) | 行为模块边界与因果组合 |
| [Jackson，Design Moves for Software](https://essenceofsoftware.com/posts/design-moves/) | 拆分/合并、统一/特化、收紧/放松 |
| [ub-mode](https://github.com/unclebob/ub-mode/blob/master/SKILL.md) | 短规则、检查前提、先删复杂性与可验证工作的写法参考 |

Markdown 节、`coverage`、`app`/`include`、查询 API、分支解释、提示词选择器与决策 YAML 是本地约定。
目录结构与 Sync/Facade 命名是工程选择。

[概念与同步关系图](map-format.md)投影本地 CONCEPT/SYNCS 引用。
解析器、哈希身份与 ARCHITECTURE.md 布局是本仓库选择，不是 Jackson 的目的依赖图。

规格维护流程改编自 [wyx v0.26.0](https://github.com/jlifyio/wyx)，保留其 [MIT 许可声明](#wyx-mit)。

## wyx (MIT)

```text
MIT License

Copyright (c) 2026 jlifyio

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
