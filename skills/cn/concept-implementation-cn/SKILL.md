---
name: concept-implementation-cn
description: Generates a modular-monolith mapping from a confirmed concept model only when the user explicitly invokes $concept-implementation-cn. / 仅在用户显式调用 $concept-implementation-cn 时做模块单体映射。
metadata:
  language: zh-CN
  translation_of: concept-implementation
  openclaw:
    homepage: https://github.com/ontology-of-everything/concept-skills/tree/main/skills/cn/concept-implementation-cn
---

# 概念实现（模块单体）

焦点问题：如何把已确认概念行为实现为可验证、可组合的模块？仅在显式调用 `$concept-implementation-cn` 时运行。按请求交付方案或实际代码；明确部分继续，影响实现的模型缺口回 concept-design-cn。

## 模块与组合

概念模块封装 state、不变量、actions/query，模块互不引用。port 声明接口，adapter 实现接口；domain 不依赖协议或其他概念。sync 组合层承载跨概念业务策略，组合根装配实现，接口适配器转换 DTO/协议并调用组合入口。

**同步可收窄行为，不可扩展契约**：组合只调用契约允许的行为；前置条件、不变量、效果及输出 case 由概念动作保证，组合查询不能替代原子检查。

OP 验证概念目的，端到端场景验证应用目的；符合规格不证明模型适切，目的落空的反例须回查模型。

## 实现约束

- API（含查询）遵守已确认的协调/权限策略；一次入口可触发多条规则。
- 组合层无自有业务状态，可持久保存溯源、重试和幂等记录。
- 错误是可匹配输出 case，须有响应、重试、补偿或有意忽略策略；事务不能代替失败契约。
- 已确认新行为先改规格再改实现；分组只解决工程组织痛点。

## 实现与验证

1. **核实输入**：读 [规格契约](references/spec-format.md)，再读应用目的、概念模型及两层论证前提、共存/暂存规格和项目约定；已有代码沿入口核实公开动作、持久化、失败路径和测试。模型缺陷回 design，纯转录错误回 prd，代码违约在此修复。
2. **映射模块**：一个 concept 对应一个可验证边界的模块；独立包优选但不强制。物理状态私有，公开抽象状态供组合查询，actions 为公开服务；采用 query API 时保持声明的绑定语义；类型参数用泛型或不透明 ID，可零个或多个，不引入其他概念实体类型。
3. **实现组合**：读 [composition-layer.md](references/composition-layer.md)，默认 mediator；需按规则演进、多事件匹配或追踪时考虑引擎。核对完成事件、绑定、并发、请求关联和失败语义。接口适配器将请求/消息映射为明确入口，需响应时由协调产生结果。
4. **规格落位**：CONCEPT 随概念模块，SYNCS 随组合包；迁移暂存文件并同步总体 PRD 索引。
5. **验证行为和边界**：只读目标语言参考，把架构看护纳入 CI；将 OP 测试关联概念目的，端到端测试关联应用目的和 sync，并覆盖各自前提；组合执行中各概念的行为序列须符合自身契约。分组/拆包仅在导航、构建或团队协作有痛点时读 [scaling.md](references/scaling.md)。

## 完成条件

- 概念模块互不引用，跨概念业务策略仅在 syncs；domain 边界受测试保护并进 CI。
- 概念 OP、应用场景、动作不变量与适用的绑定、无/多匹配、失败、重放、请求隔离测试符合契约；事务保留完成动作的可观察语义。
- 规格共存且与代码一致；排除动作未被调用/暴露，未决模型前提未被实现猜测填补。
- 产品子集经依赖闭包、入口、剩余规则、外部资源及构建/feature 开关共同验证。

## 按需参考

| 场景 | 参考 |
| --- | --- |
| Rust workspace、trait/port、包级依赖看护 | [rust.md](references/rust.md) |
| Spring Modulith 模块与 verify 的边界 | [java-spring.md](references/java-spring.md) |
| TypeScript 包、组合与 dependency-cruiser | [typescript.md](references/typescript.md) |
| 工程选择的出处 | [sources.md](references/sources.md) |
