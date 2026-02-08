
```markdown
---
name: sqlmodel-task-user-models
description: Define SQLModel models for User and Task with proper ownership relation. Use when creating or modifying data schema.
---

# User & Task SQLModel Models

## Instructions

1. **User model**
   - id (primary key)
   - email (unique)
   - Optional: name, created_at

2. **Task model**
   - id (primary key)
   - title (required)
   - description (optional)
   - completed (bool, default False)
   - user_id (foreign key to User)
   - created_at, updated_at

3. **Relationships**
   - Back-populate tasks from User
   - Use sa_relationship_kwargs for cascade delete if desired

## Best Practices
- Use nullable=False where appropriate
- Add indexes on user_id + completed
- Use server_default for timestamps
- Keep models clean — no business logic here

## Example Structure

```python
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    # password_hash: str  (handled by Better Auth)
    tasks: list["Task"] = Relationship(back_populates="user")

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    completed: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    user_id: int = Field(foreign_key="user.id")
    user: User = Relationship(back_populates="tasks")