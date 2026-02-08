# Data Model: Next.js Frontend for Multi-User Todo App

## User Entity
- **Fields**:
  - id: Unique identifier for the user
  - email: User's email address (used for login)
  - password: User's hashed password
  - createdAt: Timestamp when user account was created
  - updatedAt: Timestamp when user account was last updated
- **Validation Rules**:
  - Email must be in valid email format
  - Password must meet minimum strength requirements
  - Email must be unique across all users
- **Relationships**:
  - One-to-many with Task entity (one user can have many tasks)

## Task Entity
- **Fields**:
  - id: Unique identifier for the task
  - userId: Reference to the user who owns the task
  - title: Title or description of the task
  - description: Detailed description of the task (optional)
  - completed: Boolean indicating if the task is completed
  - createdAt: Timestamp when task was created
  - updatedAt: Timestamp when task was last updated
- **Validation Rules**:
  - Title is required and must not be empty
  - Completed status defaults to false
  - UserId must correspond to a valid user
- **State Transitions**:
  - New task: completed = false
  - Task toggled: completed = !completed
  - Task deleted: record is removed from database

## Session Entity (Authentication)
- **Fields**:
  - sessionId: Unique identifier for the session
  - userId: Reference to the authenticated user
  - token: JWT token for authentication
  - expiresAt: Expiration timestamp for the token
  - createdAt: Timestamp when session was created
- **Validation Rules**:
  - Token must be valid JWT
  - Session must not be expired
  - User must exist when session is created