---
name: neon-postgres-setup
description: Configure Neon Serverless PostgreSQL connection with SQLModel for the Todo app. Use for database initialization and connection setup.
---

# Neon PostgreSQL + SQLModel Setup

## Instructions

1. **Environment variables**
   - Read NEON_DATABASE_URL from .env
   - Set echo=True in development only

2. **Connection engine**
   - Create SQLAlchemy engine with async support if needed
   - Use create_async_engine for async FastAPI

3. **Session management**
   - Define get_session dependency for FastAPI
   - Use context manager for sessions

4. **Initial setup**
   - Run create_all() or Alembic migration on startup (dev only)

## Best Practices
- Never hardcode credentials
- Use connection pooling (default in SQLAlchemy)
- Validate URL format early
- Log connection success/failure
- Separate dev vs prod settings

## Example Structure

```python
# database.py
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("NEON_DATABASE_URL")
engine = create_engine(DATABASE_URL, echo=True)           # sync for simple cases
# async_engine = create_async_engine(DATABASE_URL)

def get_session() -> Session:
    with Session(engine) as session:
        yield session

# For async:
# async def get_async_session() -> AsyncSession:
#     async with AsyncSession(async_engine) as session:
#         yield session

def init_db():
    SQLModel.metadata.create_all(engine)