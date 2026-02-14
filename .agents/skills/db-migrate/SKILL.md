---
name: db-migrate
description: Database migration management - Use Flyway and Atlas for version-controlled database schema migrations
---

# Database Migration Skill

## 📋 Overview

Provides two modern database migration tools:

- **Flyway**: Mature and stable, based on versioned SQL scripts
- **Atlas**: Modern, declarative schema management

## 🔧 Prerequisites

### Flyway

| Tool | Installation |
|------|--------------|
| Java 11+ | [adoptium.net](https://adoptium.net/) |
| Flyway CLI | [Download](https://flywaydb.org/download) |

### Atlas

| Tool | Windows | Linux/Mac |
|------|---------|-----------|
| Atlas | `scoop install atlas` | `brew install ariga/tap/atlas` |

## 🚀 Usage

### Flyway Migration

**Create migration script:**

```bash
.\.agent\skills\db-migrate\scripts\flyway-create.ps1 -Name "add_users_table"
# Generates: V1__add_users_table.sql
```

**Execute migration:**

```bash
.\.agent\skills\db-migrate\scripts\flyway-migrate.ps1
```

**Rollback migration:**

```bash
.\.agent\skills\db-migrate\scripts\flyway-undo.ps1
```

### Atlas Migration

**Schema diff:**

```bash
.\.agent\skills\db-migrate\scripts\atlas-diff.ps1
```

**Auto-generate migration:**

```bash
.\.agent\skills\db-migrate\scripts\atlas-migrate.ps1 -Auto
```

## 🎯 Features

### Flyway

- ✅ Versioned SQL migrations (V1__xxx.sql)
- ✅ Repeatable migrations (R__xxx.sql)
- ✅ Rollback support
- ✅ Migration history tracking

### Atlas

- ✅ Declarative schema definition (HCL)
- ✅ Auto-generated migration scripts
- ✅ Visual schema diff
- ✅ Linting and validation

## 📊 Migration Script Examples

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

## 🔗 Related Resources

- [Flyway Documentation](https://flywaydb.org/documentation/)
- [Atlas Documentation](https://atlasgo.io/getting-started)
