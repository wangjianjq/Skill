---
name: generate-changelog
description: Auto-generate project changelog
---

# Generate Changelog

Automatically generate changelog based on Git commit history.

## When to Use

- Before releasing a new version
- When summarizing project changes
- Generating release notes

## Execution Steps

1. Get recent Git commits
2. Group by type (features, fixes, refactors, etc.)
3. Generate formatted changelog

## Command

```bash
git log --oneline --pretty=format:"%h - %s (%an, %ar)" --since="30 days ago"
```

## Expected Result

Generates a changelog containing all commits from the last 30 days, sorted in reverse chronological order.
