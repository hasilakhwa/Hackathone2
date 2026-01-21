# API Contract: Task Management Endpoints

## Overview
This document defines the API contracts for the task management functionality. All endpoints require JWT authentication in the Authorization header.

## Authentication
All endpoints require a valid JWT token passed in the Authorization header:
```
Authorization: Bearer <jwt-token>
```

## Base URL
```
https://api.example.com/api/{user_id}/
```

## Endpoints

### GET /tasks
**Description**: Retrieve all tasks for the authenticated user

**Headers**:
- Authorization: Bearer `<valid-jwt-token>`

**Parameters**:
- None

**Response**:
- 200: Successful response
  ```json
  {
    "tasks": [
      {
        "id": 1,
        "title": "Sample task",
        "description": "Task description",
        "completed": false,
        "created_at": "2026-01-20T10:00:00Z",
        "updated_at": "2026-01-20T10:00:00Z",
        "user_id": 1
      }
    ]
  }
  ```
- 401: Unauthorized (invalid/missing JWT)
- 403: Forbidden (attempting to access another user's tasks)

### POST /tasks
**Description**: Create a new task for the authenticated user

**Headers**:
- Authorization: Bearer `<valid-jwt-token>`

**Request Body**:
```json
{
  "title": "New task",
  "description": "Task description (optional)",
  "completed": false
}
```

**Response**:
- 201: Created
  ```json
  {
    "id": 1,
    "title": "New task",
    "description": "Task description (optional)",
    "completed": false,
    "created_at": "2026-01-20T10:00:00Z",
    "updated_at": "2026-01-20T10:00:00Z",
    "user_id": 1
  }
  ```
- 400: Bad Request (invalid input)
- 401: Unauthorized (invalid/missing JWT)
- 403: Forbidden (attempting to create task for another user)

### GET /tasks/{id}
**Description**: Retrieve a specific task by ID

**Headers**:
- Authorization: Bearer `<valid-jwt-token>`

**Parameters**:
- id: Task ID (path parameter)

**Response**:
- 200: Successful response
  ```json
  {
    "id": 1,
    "title": "Sample task",
    "description": "Task description",
    "completed": false,
    "created_at": "2026-01-20T10:00:00Z",
    "updated_at": "2026-01-20T10:00:00Z",
    "user_id": 1
  }
  ```
- 401: Unauthorized (invalid/missing JWT)
- 403: Forbidden (attempting to access another user's task)
- 404: Not Found (task doesn't exist)

### PUT /tasks/{id}
**Description**: Update an existing task

**Headers**:
- Authorization: Bearer `<valid-jwt-token>`

**Parameters**:
- id: Task ID (path parameter)

**Request Body**:
```json
{
  "title": "Updated task title",
  "description": "Updated description",
  "completed": true
}
```

**Response**:
- 200: Successful update
  ```json
  {
    "id": 1,
    "title": "Updated task title",
    "description": "Updated description",
    "completed": true,
    "created_at": "2026-01-20T10:00:00Z",
    "updated_at": "2026-01-20T11:00:00Z",
    "user_id": 1
  }
  ```
- 400: Bad Request (invalid input)
- 401: Unauthorized (invalid/missing JWT)
- 403: Forbidden (attempting to update another user's task)
- 404: Not Found (task doesn't exist)

### DELETE /tasks/{id}
**Description**: Delete a specific task

**Headers**:
- Authorization: Bearer `<valid-jwt-token>`

**Parameters**:
- id: Task ID (path parameter)

**Response**:
- 204: Successfully deleted
- 401: Unauthorized (invalid/missing JWT)
- 403: Forbidden (attempting to delete another user's task)
- 404: Not Found (task doesn't exist)

### PATCH /tasks/{id}/complete
**Description**: Toggle the completion status of a task

**Headers**:
- Authorization: Bearer `<valid-jwt-token>`

**Parameters**:
- id: Task ID (path parameter)

**Response**:
- 200: Successful update
  ```json
  {
    "id": 1,
    "title": "Sample task",
    "description": "Task description",
    "completed": true,
    "created_at": "2026-01-20T10:00:00Z",
    "updated_at": "2026-01-20T11:00:00Z",
    "user_id": 1
  }
  ```
- 401: Unauthorized (invalid/missing JWT)
- 403: Forbidden (attempting to modify another user's task)
- 404: Not Found (task doesn't exist)