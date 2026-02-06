---
name: generate-changelog
description: 自动生成项目变更日志
---

# Generate Changelog

基于 Git 提交历史自动生成变更日志。

## 何时使用

- 发布新版本前
- 需要总结项目变更
- 生成发布说明

## 执行步骤

1. 获取最近的 Git 提交
2. 按类型分组（功能、修复、重构等）
3. 生成格式化的变更日志

## 命令

```bash
git log --oneline --pretty=format:"%h - %s (%an, %ar)" --since="30 days ago"
```

## 预期结果

生成包含最近 30 天所有提交的变更日志，按时间倒序排列。
