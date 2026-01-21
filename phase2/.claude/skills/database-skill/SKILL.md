---
name: database-skill
description: Design database schemas, create tables, and manage migrations with best practices. Use for relational database development (e.g., PostgreSQL, MySQL).
---

# Database Skill – Schema Design & Migrations

## Instructions

1. **Schema Design**
   - Identify entities and relationships
   - Normalize data (up to 3NF unless justified)
   - Define primary keys and foreign keys
   - Use appropriate data types and constraints

2. **Table Creation**
   - Create tables with clear, consistent naming
   - Enforce NOT NULL, UNIQUE, and CHECK constraints
   - Add indexes for frequently queried columns
   - Use timestamps for auditing (`created_at`, `updated_at`)

3. **Migrations**
   - Version-controlled, incremental changes
   - Forward-only, reversible when possible
   - Separate schema changes from data backfills
   - Ensure migrations are idempotent and safe for production

4. **Relationships & Integrity**
   - Use foreign key constraints
   - Define ON DELETE / ON UPDATE rules explicitly
   - Avoid cascading deletes unless intentional
   - Prefer soft deletes where data recovery matters

## Best Practices
- Use snake_case for table and column names
- Keep migrations small and focused
- Never modify old migrations in shared environments
- Document schema decisions and trade-offs
- Test migrations on staging before production
- Optimize for read/write patterns, not just normalization

## Example Schema & Migration

```sql
-- users table
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

-- posts table
CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
  title VARCHAR(200) NOT NULL,
  body TEXT,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_posts_user_id ON posts(user_id);
