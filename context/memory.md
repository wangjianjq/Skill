# Architectural Decision Records (ADR) - AI Memory

## Schema: Memory Configuration

- document_type: architectural_decision_records
- target_audience: ai_agents
- enforcement_level: mandatory
- read_frequency: every_session_start
- scope: long_term_memory

---

## [ADR-001] Hybrid Intelligence Architecture
- **Decision**: Adopt "Passive Context (Brain) + Active Skills (Hands)" architecture.
- **Rationale**: Balances context awareness with modular tool execution.

## [ADR-002] Security: Disable Eval
- **Decision**: Globally forbid `eval` in all scripts. Use list-based subprocess calls or array expansions.
- **Rationale**: Mitigate command injection risks.

## [ADR-003] Language: Cognitive Mirroring
- **Decision**: Implement "Cognitive Mirroring Protocol".
- **Rule**: AI must match the user's dialogue language for meta-cognition (tasks, plans, chat).
- **Note**: Internal AI-only docs (e.g., status.md) should prefer English for efficiency.

## [ADR-004] Protocol Maintenance Authorization
- **Decision**: Modifications to `.agents/` are permitted ONLY under explicit user authorization.
- **Session Note**: 2026-02-14 session has been granted maintenance access for logic alignment.

## [ADR-005] God Mode: Global Sovereignty Injection
- **Decision**: Mandatory implementation of "God Mode" [GOD_MODE_SOP] in all AI tools' global system prompts.
- **Rationale**: To eliminate "Cold Start" failures and ensure AI agents always operate under project governance regardless of the entry point.
