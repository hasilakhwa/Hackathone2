# Quickstart: FastAPI JWT-Secured Task Endpoints

## Prerequisites

- Python 3.9+
- Poetry or pip for dependency management
- Existing database setup from previous spec (SQLModel models, database connection)
- BETTER_AUTH_SECRET environment variable configured

## Installation

### 1. Install Dependencies

```bash
cd backend
pip install fastapi uvicorn python-jose[cryptography] python-multipart
```

Or if using Poetry:

```bash
cd backend
poetry add fastapi uvicorn python-jose[cryptography] python-multipart
```

### 2. Environment Configuration

Ensure your `.env` file contains the BETTER_AUTH_SECRET variable:

```env
BETTER_AUTH_SECRET=your-super-secret-key-here
NEON_DATABASE_URL=postgresql://...
```

### 3. Project Structure

Create the necessary files for the API implementation:

```bash
backend/
├── src/
│   ├── routers/
│   │   └── tasks.py
│   ├── dependencies/
│   │   └── auth.py
│   ├── schemas/
│   │   └── task.py
│   └── main.py
```

## API Usage

### 1. Start the Server

```bash
cd backend
uvicorn src.main:app --reload
```

### 2. API Endpoints

All endpoints require JWT authentication. Example request with curl:

```bash
# List user's tasks
curl -X GET http://localhost:8000/api/1/tasks \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"

# Create a new task
curl -X POST http://localhost:8000/api/1/tasks \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{
    "title": "New Task",
    "description": "Task description",
    "completed": false
  }'

# Get a specific task
curl -X GET http://localhost:8000/api/1/tasks/1 \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"

# Update a task
curl -X PUT http://localhost:8000/api/1/tasks/1 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{
    "title": "Updated Task",
    "description": "Updated description",
    "completed": true
  }'

# Toggle task completion
curl -X PATCH http://localhost:8000/api/1/tasks/1/complete \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{
    "completed": true
  }'

# Delete a task
curl -X DELETE http://localhost:8000/api/1/tasks/1 \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

### 3. Security Features

- All endpoints follow the /api/{user_id}/tasks pattern with proper user_id validation
- JWT authentication required for all endpoints
- User isolation: Users can only access their own tasks
- Proper HTTP status codes:
  - 200 OK: Successful GET/PUT/PATCH requests
  - 201 Created: Successful POST request
  - 204 No Content: Successful DELETE request
  - 401 Unauthorized: Invalid/missing JWT token
  - 403 Forbidden: User ID mismatch in path vs token
  - 404 Not Found: Task not found or doesn't belong to user

## Development Commands

### Run the API Server

```bash
cd backend
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

### Access API Documentation

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Run Tests

```bash
pytest tests/
```

## Security Notes

- Always validate JWT tokens before processing requests
- Ensure user_id in URL path matches the authenticated user_id
- All sensitive operations require proper authentication and authorization
- Use HTTPS in production to protect JWT tokens in transit
- Tokens should have appropriate expiration times for security