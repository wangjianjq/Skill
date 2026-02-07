# Decision Memory (TOC)

1. [ADR-001] Architecture: Hybrid Intelligence
2. [ADR-002] Security Audit: Disable Eval
3. [ADR-003] Language Protocol: Cognitive Mirroring

## [ADR-001] Architecture: Hybrid Intelligence

- Decision: Adopt "Passive Context (Brain) + Active Skills (Hands)" architecture.
- Rationale: Vercel research proves passive context is most effective for knowledge retrieval, while Skills are most stable for executing specific actions (e.g., formatting).

## [ADR-002] Security Audit: Disable Eval

- Decision: Globally disable `eval` in shell scripts, use array expansion instead.
- Rationale: Prevent command injection vulnerabilities.

## [ADR-003] Language Protocol: Cognitive Mirroring

- Decision: Implement "Cognitive Mirroring Protocol" to enforce AI matching user's dialogue language.
- Rationale: Ensure seamless user experience with consistent language in all AI-generated artifacts.
