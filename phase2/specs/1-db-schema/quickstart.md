# Quickstart: Database Schema Setup

## Prerequisites

- Python 3.9+
- Poetry or pip for dependency management
- Neon Serverless PostgreSQL account
- Environment variable `NEON_DATABASE_URL` configured

## Installation

### 1. Install Dependencies

```bash
cd backend
pip install sqlmodel sqlalchemy psycopg2-binary python-dotenv
```

Or if using Poetry:

```bash
cd backend
poetry add sqlmodel sqlalchemy psycopg2-binary python-dotenv
```

### 2. Environment Configuration

Create a `.env` file in the backend directory with your Neon PostgreSQL connection string:

```env
NEON_DATABASE_URL=postgresql://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname?sslmode=require
```

### 3. Initialize Database Models

```python
from backend.src.core.database import init_db

# Initialize database tables
init_db()
```

## Usage

### 1. Import Models and Database Components

```python
from backend.src.models import User, Task
from backend.src.core.database import get_session, create_user, create_task, get_tasks_by_user_id
```

### 2. Create Sample User

```python
from backend.src.core.database import create_user

def example_create_user():
    with get_session() as session:
        user = create_user(session, "example@example.com")
        return user
```

### 3. Create Sample Task

```python
from backend.src.core.database import create_task

def example_create_task(user_id: int):
    with get_session() as session:
        task = create_task(session, "Sample Task", "Task description", user_id)
        return task
```

### 4. Query Tasks by User

```python
from backend.src.core.database import get_tasks_by_user_id

def example_get_user_tasks(user_id: int):
    with get_session() as session:
        tasks = get_tasks_by_user_id(session, user_id)
        return tasks
```

## Development Commands

### Initialize Database Tables

```bash
python -c "from backend.src.core.database import init_db; init_db()"
```

### Run Tests

```bash
cd backend
pytest tests/
```

### Run Individual Test Suites

```bash
# Run unit tests
pytest tests/unit/

# Run integration tests
pytest tests/integration/
```

## Database Schema Overview

### User Model
- `id`: Primary key, auto-incrementing integer
- `email`: Unique string (max 255 chars), required
- `created_at`: Timestamp, defaults to current time
- `updated_at`: Timestamp, defaults to current time

### Task Model
- `id`: Primary key, auto-incrementing integer
- `title`: String (max 255 chars), required, min length 1
- `description`: Optional string (max 1000 chars)
- `completed`: Boolean, defaults to False
- `created_at`: Timestamp, defaults to current time
- `updated_at`: Timestamp, defaults to current time
- `user_id`: Foreign key to users.id, required, indexed

## Security Notes

- Database enforces user isolation through foreign key constraints
- Always validate that the user requesting data owns that data
- Use the user_id from the authenticated session, not from user input
- Foreign key constraints prevent orphaned tasks
- Unique constraint on User.email prevents duplicate accounts