---
name: sql-lint
description: SQL 代码规范检查 - 使用 SQLFluff 检查 SQL 语句风格和语法（支持 PostgreSQL, MySQL, SQLite 等）
---

# SQL Lint Skill

## 📋 概述

使用 **SQLFluff** 检查 SQL 代码质量，支持多种数据库方言：

- PostgreSQL, MySQL, MariaDB
- SQLite, BigQuery, Snowflake
- Redshift, TSQL, Oracle 等

## 🔧 前置条件

| 工具 | 安装命令 |
|-----|---------|
| Python 3.8+ | [python.org](https://python.org) |
| SQLFluff | `pip install sqlfluff` |

## 🚀 使用方法

**检查单个文件:**

```bash
.\.agent\skills\sql-lint\scripts\lint.ps1 -File query.sql
```

**指定数据库方言:**

```bash
.\.agent\skills\sql-lint\scripts\lint.ps1 -Dialect postgres
```

**自动修复:**

```bash
.\.agent\skills\sql-lint\scripts\lint.ps1 -Fix
```

## 🎯 检查内容

- ✅ SQL 关键字大小写一致性
- ✅ 缩进和格式规范
- ✅ JOIN 类型明确性
- ✅ 表别名使用规范
- ✅ WHERE 条件安全性

## 📊 支持的数据库方言

| 方言名 | 数据库 |
|-------|-------|
| `postgres` | PostgreSQL |
| `mysql` | MySQL/MariaDB |
| `sqlite` | SQLite |
| `bigquery` | Google BigQuery |
| `snowflake` | Snowflake |
| `tsql` | SQL Server |

## ⚙️ 配置示例

创建 `.sqlfluff`:

```ini
[sqlfluff]
dialect = postgres
templater = jinja
exclude_rules = L003,L009

[sqlfluff:indentation]
indent_unit = space
tab_space_size = 2

[sqlfluff:rules:L010]
capitalisation_policy = upper
```

## 🔗 相关资源

- [SQLFluff 文档](https://docs.sqlfluff.com/)
- [SQL 风格指南](https://www.sqlstyle.guide/)
