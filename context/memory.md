# 决策记忆库 (TOC)

1. [ADR-001] 架构转型: 混合智能
2. [ADR-002] 安全审计: 禁用 Eval
3. [ADR-003] 语言协议: 认知镜像

## [ADR-001] 架构转型: 混合智能

- 决定: 采用 "Passive Context (Brain) + Active Skills (Hands)" 架构。
- 原因: Vercel 研究证明被动上下文对知识检索最有效，而 Skils 对执行具体动作（如 formatting）最稳定。

## [ADR-002] 安全审计: 禁用 Eval

- 决定: 全局禁用 shell 脚本中的 `eval`，改用数组扩展。
- 原因: 2026-02-05 安全审计发现潜在注入风险 (lint.sh)。

## [ADR-003] 语言协议: 认知镜像

- 决定: 实施 "Cognitive Mirroring Protocol"，强制 AI 用此匹配用户对话语言。
- 原因: 用户要求元认知工件（Task/Plan）必须本地化，以提升协作体验。
