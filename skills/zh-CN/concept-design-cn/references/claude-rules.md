# 校准 CLAUDE.md

对照确认契约、实际代码与[工程架构](architecture.md)，报告冲突后更新相关规则；不得把现状当契约或改契约掩盖缺陷。
用下列短原则替换重复表述，保留无关规则与未决事项。每条关联项目内权威定义和实际检查，不复制规格正文。

```markdown
1. 目录固定 entry/<模块>、compositions/<分组>、concepts/<概念>、bootstrap；业务目录小写单数，组合分组与规格同名，概念内按 api/application/domain/adapters 分责。
2. Entry → Facade → Synchronization → 概念 API；Facade 每个操作只转发一次，同步显式组织业务决策；同步不互调、不回调 Facade，辅助组件不反调。
3. 概念独占状态与不变量，禁止概念互依、互调、互读；业务访问只用 api，装配用专属入口。application 依赖 api/domain 和内部端口，adapters 实现端口；api/domain 不依赖概念其他层，以上业务层独立于框架。
4. 按 CONCEPT.md/SYNCS.md 实现；行为变更先确认契约。用业务范围命名 Facade、业务动作命名 Synchronization，列表与集合按语义用复数；规则映射和持久身份保持一致。
5. 架构检查覆盖目录、命名、依赖、可见性和转发；行为测试覆盖契约与执行边界。失败改代码，未验证不报通过。
```

按项目语言与已确认例外落实名称和检查入口；核对生成规则与三方一致，报告未解冲突和未执行检查。
