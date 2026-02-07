# Skill: Internationalization (i18n) Enforcement

> **Skill ID**: `SKILL_I18N`
> **Tags**: `i18n`, `multi-language`, `localization`
> **Version**: 1.0

## 1. The i18n Gate (Mandatory Protocol)

**Trigger**: Whenever the project requires multi-language support or when modifying existing localized features.

### 1.1 Language Discovery (Initialization)

If internationalization is required but no language list exists:

- **Rule**: The AI MUST ask: "Which languages do you want this project to support? (e.g., English, Chinese, Japanese)".
- **Action**: Create a file named `PROJECT_LANGUAGES.md` in the project root with the confirmed list.

**Format for `PROJECT_LANGUAGES.md`**:

```markdown
# Project Supported Languages
- [x] English (en)
- [x] Chinese (zh-CN)
...
```

### 1.2 Mandatory Retrieval (Execution)

- **Constraint**: Before ANY code generation or modification, the AI **MUST** read `PROJECT_LANGUAGES.md`.
- **Enforcement**: Ensure that every new feature, UI string, or functional content is adapted to ALL languages listed in the markdown file.

## 2. Technical Implementation Standards

- **Rule 1**: Avoid hardcoding strings in the UI. Use resources/localization files (e.g., `i18n.json`, `gettext`, or platform-specific resources).
- **Rule 2**: If the user project uses a specific i18n framework (e.g., `react-i18next`, `intl`, `gettext`), adhere strictly to that framework's patterns.
- **Rule 3**: New languages added to `PROJECT_LANGUAGES.md` later require a "Retroactive Adaptation" check for existing features.

## 3. Verification

- After implementation, verify that the translation files/resources for ALL listed languages have been updated consistently.
