# Database: PostgreSQL

## [Modern] (v16+, Vector)

* **Version**: 16+ support for specific JSONB optimizations and `pgvector`.
* **Primary Key**: UUIDv7 (time-sortable).
* **Storage**: Heavy use of `JSONB` for schema-less partitions.

### Modern Golden Snippet

```sql
SELECT * FROM documents ORDER BY embedding <-> '[1,2,3]' LIMIT 5;
```

## [Legacy] (v11 - v15)

* **Version**: 11+.
* **Primary Key**: `serial` or UUIDv4.
* **Patterns**: Traditional relational schema, limited JSONB indexing.
