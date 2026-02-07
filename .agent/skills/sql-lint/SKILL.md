---
name: sql-lint
description: SQL code style check - Use SQLFluff to check SQL statement style and syntax (supports PostgreSQL, MySQL, SQLite, etc.)
---

# SQL Lint Skill

## 📋 Overview

Use **SQLFluff** to check SQL code quality, supporting multiple database dialects:

- PostgreSQL, MySQL, MariaDB
- SQLite, BigQuery, Snowflake
- Redshift, TSQL, Oracle, etc.

## 🔧 Prerequisites

| Tool | Installation |
|------|--------------|
| Python 3.8+ | [python.org](https://python.org) |
| SQLFluff | `pip install sqlfluff` |

## 🚀 Usage

**Check single file:**

```bash
.\.agent\skills\sql-lint\scripts\lint.ps1 -File query.sql
```

**Specify database dialect:**

```bash
.\.agent\skills\sql-lint\scripts\lint.ps1 -Dialect postgres
```

**Auto-fix:**

```bash
.\.agent\skills\sql-lint\scripts\lint.ps1 -Fix
```

## 🎯 What It Checks

- ✅ SQL keyword case consistency
- ✅ Indentation and formatting standards
- ✅ JOIN type clarity
- ✅ Table alias usage standards
- ✅ WHERE condition safety

## 📊 Supported Database Dialects

| Dialect | Database |
|---------|----------|
| `postgres` | PostgreSQL |
| `mysql` | MySQL/MariaDB |
| `sqlite` | SQLite |
| `bigquery` | Google BigQuery |
| `snowflake` | Snowflake |
| `tsql` | SQL Server |

## ⚙️ Configuration Example

Create `.sqlfluff`:

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

## 🔗 Related Resources

- [SQLFluff Documentation](https://docs.sqlfluff.com/)
- [SQL Style Guide](https://www.sqlstyle.guide/)
