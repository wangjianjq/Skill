# Skill: Architectural Governance

> **Skill ID**: `SKILL_ARCHITECT`
> **Tags**: `architecture`, `design-patterns`, `rigor`, `structural-governance`
> **Version**: 1.0

## 1. Structural Rigor (Mandatory)

**Trigger**: Before starting any non-trivial feature or project initialization.

### 1.1 Structural Audit

The AI must define the architectural pattern:

- **Criteria**: Is it a Monolith, Microservice, Layered (N-Tier), or Hexagonal (Ports & Adapters)?
- **Requirement**: Create an index file `ARCHITECTURE.md` in the project root if it doesn't exist.

### 1.2 Design Principles (Enforcement)

- **SOLID**: Every change must adhere to Single Responsibility and Open-Closed principles.
- **DRY/AHA**: Prioritize "Avoid Hasty Abstractions" over "Don't Repeat Yourself". Maintain code readability.
- **Dependency Rule**: Inner layers (Domain/Business Logic) must not depend on outer layers (Infrastructure/UI).

## 2. Technical Debt & Safety

- **Rule 1**: No "God Objects". Classes/Models must have specific bounded contexts.
- **Rule 2**: Security-First. Inputs MUST be validated; secrets MUST be stored in `.env` (never committed).
- **Rule 3**: Performance. Optimize O(n^2) operations or justify them in comments.

## 3. Governance Workflow

### 3.1 Architectural Review

Before implementing a complex story:

1. **Define**: Briefly outline the data flow and class relationships.
2. **Review**: Check for circular dependencies.
3. **Ratify**: Document the decision in `PROJECT_STATUS.md` under "Architectural Decisions".

## 4. Design Patterns (The "Super Architect" Toolkit)

The AI should proactively suggest:

- **Factory/Builder**: For complex object creation.
- **Strategy**: For interchangeable algorithms.
- **Observer**: For decoupled event handling.
- **Adapter**: For integrating third-party libraries (especially i18n/Design).
