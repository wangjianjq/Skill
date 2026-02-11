# 决策记忆库 (TOC)

## Schema: Memory Configuration

- document_type: architectural_decision_records
- target_audience: ai_agents
- enforcement_level: mandatory
- read_frequency: every_session_start
- scope: long_term_memory

1. [ADR-001] 架构转型: 混合智能
2. [ADR-002] 安全审计: 禁用 Eval
3. [ADR-003] 语言协议: 认知镜像

## [ADR-001] 架构转型: 混合智能

- 决定: 采用 "Passive Context (Brain) + Active Skills (Hands)" 架构。

## [ADR-002] 安全审计: 禁用 Eval

- 决定: 全局禁用 shell 脚本中的 `eval`，改用数组扩展。

## [ADR-003] 语言协议: 认知镜像

- 决定: 实施 "Cognitive Mirroring Protocol"，强制 AI 用此匹配用户对话语言。
