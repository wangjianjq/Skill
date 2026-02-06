---
name: db-migrate
description: 数据库迁移管理 - 使用 Flyway 和 Atlas 进行版本控制的数据库 Schema 迁移
---

# Database Migration Skill

## 📋 概述

提供两种现代化的数据库迁移工具：

- **Flyway**: 成熟稳定，基于版本化 SQL 脚本
- **Atlas**: 现代化，声明式 Schema 管理

## 🔧 前置条件

### Flyway

| 工具 | 安装命令 |
|-----|---------|
| Java 11+ | [adoptium.net](https://adoptium.net/) |
| Flyway CLI | [下载](https://flywaydb.org/download) |

### Atlas

| 工具 | 安装命令 (Windows) | 安装命令 (Linux/Mac) |
|-----|-----------------|------------------|
| Atlas | `scoop install atlas` | `brew install ariga/tap/atlas` |

## 🚀 使用方法

### Flyway 迁移

**创建迁移脚本:**

```bash
.\.agent\skills\db-migrate\scripts\flyway-create.ps1 -Name "add_users_table"
# 生成: V1__add_users_table.sql
```

**执行迁移:**

```bash
.\.agent\skills\db-migrate\scripts\flyway-migrate.ps1
```

**回滚迁移:**

```bash
.\.agent\skills\db-migrate\scripts\flyway-undo.ps1
```

### Atlas 迁移

**Schema 对比:**

```bash
.\.agent\skills\db-migrate\scripts\atlas-diff.ps1
```

**自动生成迁移:**

```bash
.\.agent\skills\db-migrate\scripts\atlas-migrate.ps1 -Auto
```

## 🎯 功能特性

### Flyway

- ✅ 版本化 SQL 迁移（V1__xxx.sql）
- ✅ 可重复迁移（R__xxx.sql）
- ✅ 回滚支持
- ✅ 迁移历史追踪

### Atlas

- ✅ 声明式 Schema 定义（HCL）
- ✅ 自动生成迁移脚本
- ✅ Schema 可视化对比
- ✅ Linting 和验证

## 📊 迁移脚本示例

**Flyway (V1__create_users.sql):**

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
```

**Atlas (schema.hcl):**

```hcl
table "users" {
  schema = schema.public
  column "id" {
    type = serial
  }
  column "username" {
    type = varchar(50)
    null = false
  }
  primary_key {
    columns = [column.id]
  }
  index "idx_users_email" {
    columns = [column.email]
  }
}
```

## 🔗 相关资源

- [Flyway 文档](https://flywaydb.org/documentation/)
- [Atlas 文档](https://atlasgo.io/getting-started)
