# Quickstart Guide: Backend API & Data Layer

## Prerequisites
- Python 3.11+
- Poetry or pip for dependency management
- Neon PostgreSQL account with connection details
- Environment variables configured for database and JWT secret

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Install dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   # OR if using poetry
   poetry install
   ```

3. **Configure environment variables**
   Create a `.env` file with the following:
   ```env
   DATABASE_URL=postgresql+asyncpg://username:password@ep-xxx.us-east-1.aws.neon.tech/dbname
   BETTER_AUTH_SECRET=your-jwt-secret-here
   ```

4. **Run database migrations**
   ```bash
   python -m alembic upgrade head
   ```

5. **Start the development server**
   ```bash
   uvicorn src.main:app --reload --port 8000
   ```

## API Endpoints

Once running, the API will be available at `http://localhost:8000` with the following endpoints:
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

## Testing

Run the test suite:
```bash
pytest tests/
```

## Configuration Files

- `src/core/config.py` - Application configuration
- `src/core/database.py` - Database connection settings
- `src/core/security.py` - JWT and authentication settings