# API Contracts: Frontend-Backend Integration for Todo App

## Authentication Endpoints

### POST /api/auth/register
- **Description**: Register a new user account
- **Request**:
  - Headers: Content-Type: application/json
  - Body: {email: string, password: string}
- **Response**:
  - Success: 200 {success: boolean, user: {id, email}}
  - Error: 400 {error: string}
- **Authentication**: None (public)

### POST /api/auth/login
- **Description**: Authenticate user and return session
- **Request**:
  - Headers: Content-Type: application/json
  - Body: {email: string, password: string}
- **Response**:
  - Success: 200 {success: boolean, user: {id, email}, token: string}
  - Error: 401 {error: string}
- **Authentication**: None (public)

### POST /api/auth/logout
- **Description**: Log out the current user
- **Request**:
  - Headers: Authorization: Bearer {token}
- **Response**:
  - Success: 200 {success: boolean}
  - Error: 401 {error: string}
- **Authentication**: JWT Token Required

## Task Management Endpoints

### GET /api/{userId}/tasks
- **Description**: Retrieve all tasks for the authenticated user
- **Path Parameters**: userId (string)
- **Headers**: Authorization: Bearer {token}
- **Response**:
  - Success: 200 [{id, userId, title, description, completed, createdAt, updatedAt}]
  - Error: 401 {error: string}, 403 {error: string}
- **Authentication**: JWT Token Required

### POST /api/{userId}/tasks
- **Description**: Create a new task for the user
- **Path Parameters**: userId (string)
- **Headers**: Authorization: Bearer {token}
- **Request Body**: {title: string, description?: string}
- **Response**:
  - Success: 201 {id, userId, title, description, completed, createdAt, updatedAt}
  - Error: 400 {error: string}, 401 {error: string}
- **Authentication**: JWT Token Required

### PUT /api/{userId}/tasks/{taskId}
- **Description**: Update an existing task
- **Path Parameters**: userId (string), taskId (string)
- **Headers**: Authorization: Bearer {token}
- **Request Body**: {title?: string, description?: string, completed?: boolean}
- **Response**:
  - Success: 200 {id, userId, title, description, completed, updatedAt}
  - Error: 400 {error: string}, 401 {error: string}, 404 {error: string}
- **Authentication**: JWT Token Required

### PATCH /api/{userId}/tasks/{taskId}/toggle
- **Description**: Toggle the completion status of a task
- **Path Parameters**: userId (string), taskId (string)
- **Headers**: Authorization: Bearer {token}
- **Response**:
  - Success: 200 {id, userId, title, description, completed, updatedAt}
  - Error: 401 {error: string}, 404 {error: string}
- **Authentication**: JWT Token Required

### DELETE /api/{userId}/tasks/{taskId}
- **Description**: Delete a task
- **Path Parameters**: userId (string), taskId (string)
- **Headers**: Authorization: Bearer {token}
- **Response**:
  - Success: 200 {success: boolean}
  - Error: 401 {error: string}, 404 {error: string}
- **Authentication**: JWT Token Required