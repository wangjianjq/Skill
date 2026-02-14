---
tags: ["{tag1}", "{tag2}", "{tag3}"]
---
# Language: {LANGUAGE_NAME}

## Schema: Language Specification

- language: {language_name}
- category: {programming_language|systems_programming_language|mobile_programming_language|backend_programming_language}
- latest_supported_version: {version}
- package_manager: {manager_name}
- linter: {linter_name}
- type_system: {static|dynamic|gradual}
- concurrency: {concurrency_model}
- {additional_field}: {value}

---

## 1. Modern Stack ({latest_version}+)

1.1 **Environment Manager**

- Primary: {tool_name}
- Alternative: {alt_tool}
- Config: {config_file} (mandatory|recommended)

1.2 **Linter**

- Tool: {linter_name}
- Config: {config_pattern}

1.3 **Type Annotations**

- Standard: {typing_approach}
- Features: {modern_features}

1.4 **Concurrency**

- Pattern: {async_pattern}
- Libraries: {concurrency_libs}

### Modern Snippet: {Feature_Name}

```{language}
// Example code here
```

---

## 2. Legacy Stack ({old_versions})

2.1 **Environment Manager**

- Primary: {legacy_tool}
- Config: {legacy_config}

2.2 **Linter**

- Tools: {legacy_linters}

2.3 **Type Annotations**

- Standard: {legacy_typing}
- Compatibility: {backport_notes}

2.4 **Concurrency**

- Pattern: {legacy_async}

### Legacy Snippet: {Legacy_Feature}

```{language}
// Legacy example code
```

---

## 3. Best Practices

3.1 **Code Style**

- {rule_1}
- {rule_2}
- {rule_3}

3.2 **Dependencies**

- {dependency_rule_1}
- {dependency_rule_2}

3.3 **Testing**

- {testing_framework}: {testing_approach}
- {test_pattern}: {pattern_description}

3.4 **Performance**

- {perf_tip_1}
- {perf_tip_2}

---

## 4. Critical Rules

1. **{Rule_Category_1}**: {explanation}
2. **{Rule_Category_2}**: {explanation}
3. **{Rule_Category_3}**: {explanation}
