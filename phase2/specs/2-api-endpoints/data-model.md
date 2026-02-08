# Data Model: API Request/Response Schemas

## Pydantic Schema: TaskCreate

### Fields:
- **title**: String, Required (min_length=1, max_length=255)
- **description**: String, Optional (max_length=1000)
- **completed**: Boolean, Optional, Default False

### Validation Rules:
- Title must not be empty or just whitespace
- Title must be between 1 and 255 characters
- Description can be omitted but if provided, limited to 1000 characters
- Completed field defaults to False if not provided

## Pydantic Schema: TaskRead

### Fields:
- **id**: Integer, Required (primary key from database)
- **title**: String, Required
- **description**: String, Optional
- **completed**: Boolean, Required
- **created_at**: DateTime, Required
- **updated_at**: DateTime, Required
- **user_id**: Integer, Required (foreign key to user)

### Validation Rules:
- All fields from the database Task model are included
- Immutable fields (id, created_at, user_id) cannot be modified via API
- Read-only representation of Task entity

## Pydantic Schema: TaskUpdate

### Fields:
- **title**: String, Optional (min_length=1, max_length=255)
- **description**: String, Optional (max_length=1000)
- **completed**: Boolean, Optional

### Validation Rules:
- All fields are optional to allow partial updates
- Title validation: if provided, must be 1-255 characters
- Description validation: if provided, must be ≤1000 characters
- Allows patch-like updates without requiring all fields

## Pydantic Schema: TaskToggleCompletion

### Fields:
- **completed**: Boolean, Required

### Validation Rules:
- Only the completed status can be toggled
- Used specifically for PATCH /api/{user_id}/tasks/{id}/complete endpoint

## API Endpoint Definitions

### GET /api/{user_id}/tasks
- **Request Parameters**: user_id (path), no request body
- **Response Body**: Array of TaskRead objects
- **Authentication**: JWT required
- **Authorization**: user_id in path must match authenticated user

### POST /api/{user_id}/tasks
- **Request Parameters**: user_id (path)
- **Request Body**: TaskCreate object
- **Response Body**: TaskRead object
- **Authentication**: JWT required
- **Authorization**: user_id in path must match authenticated user

### GET /api/{user_id}/tasks/{task_id}
- **Request Parameters**: user_id (path), task_id (path), no request body
- **Response Body**: TaskRead object
- **Authentication**: JWT required
- **Authorization**: user_id in path must match authenticated user AND task belongs to user

### PUT /api/{user_id}/tasks/{task_id}
- **Request Parameters**: user_id (path), task_id (path)
- **Request Body**: TaskUpdate object
- **Response Body**: TaskRead object
- **Authentication**: JWT required
- **Authorization**: user_id in path must match authenticated user AND task belongs to user

### DELETE /api/{user_id}/tasks/{task_id}
- **Request Parameters**: user_id (path), task_id (path), no request body
- **Response Body**: No content (204)
- **Authentication**: JWT required
- **Authorization**: user_id in path must match authenticated user AND task belongs to user

### PATCH /api/{user_id}/tasks/{task_id}/complete
- **Request Parameters**: user_id (path), task_id (path)
- **Request Body**: TaskToggleCompletion object
- **Response Body**: TaskRead object
- **Authentication**: JWT required
- **Authorization**: user_id in path must match authenticated user AND task belongs to user

## Authentication Flow

### JWT Token Processing:
1. Extract Authorization header with Bearer scheme
2. Decode JWT using BETTER_AUTH_SECRET from environment
3. Extract user_id from token payload
4. Compare with user_id from URL path
5. Attach user context to request for database operations

## Security Constraints:
- All endpoints require valid JWT token
- Path user_id must match authenticated user_id
- Only tasks owned by authenticated user are accessible
- Invalid tokens result in 401 Unauthorized
- User mismatch results in 403 Forbidden
- Non-existent or non-owned tasks result in 404 Not Found