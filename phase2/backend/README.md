# Todo Backend API

This is the backend API for the Todo Full-Stack Web Application, built with FastAPI and SQLModel.

## Features
- JWT-based authentication
- Task CRUD operations
- User data isolation
- PostgreSQL database with Neon

## Tech Stack
- Python 3.11
- FastAPI
- SQLModel
- Neon Serverless PostgreSQL
- PyJWT

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables by copying the example:
```bash
cp .env.example .env
# Edit .env with your actual values
```

3. Run the server:
```bash
python start_server.py
```

Or with uvicorn directly:
```bash
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

## Environment Variables

Create a `.env` file with the following variables:

```env
# Database Configuration
DATABASE_URL=postgresql+asyncpg://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname

# Authentication
BETTER_AUTH_SECRET=your-super-secret-jwt-key-change-this-in-production
JWT_ALGORITHM=HS256

# Server Configuration
HOST=0.0.0.0
PORT=8000

# API Configuration
API_V1_PREFIX=/api

# CORS Configuration
ALLOWED_ORIGINS=http://localhost,http://localhost:3000,https://localhost,https://localhost:3000

# Logging
LOG_LEVEL=INFO
```

Or copy the example:
```bash
cp .env.example .env
```

## API Endpoints

- `GET /api/{user_id}/tasks` - Retrieve user's tasks
- `POST /api/{user_id}/tasks` - Create a new task
- `GET /api/{user_id}/tasks/{id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{id}` - Update a task
- `DELETE /api/{user_id}/tasks/{id}` - Delete a task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle task completion

## Authentication

All endpoints require a valid JWT token in the Authorization header:
```
Authorization: Bearer <jwt-token-here>
```

## Development

To run tests:
```bash
pytest tests/
```

To format code:
```bash
black src/
```

To lint code:
```bash
flake8 src/
```