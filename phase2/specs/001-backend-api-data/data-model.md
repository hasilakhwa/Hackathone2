# Data Model: Backend API & Data Layer for Todo Web Application

## Task Entity

**Fields**:
- `id`: Integer (Primary Key, Auto-increment)
- `title`: String (Required, max length 255)
- `description`: String (Optional, max length 1000)
- `completed`: Boolean (Default: False)
- `created_at`: DateTime (Auto-generated on creation)
- `updated_at`: DateTime (Auto-generated on update)
- `user_id`: Integer (Foreign Key to User, Required for ownership)

**Validation Rules**:
- Title must not be empty
- Title must be less than 256 characters
- Description can be null or up to 1000 characters
- Completed status defaults to False

**Relationships**:
- Belongs to one User (Many-to-One)
- Each task is owned by exactly one user

## User Entity

**Fields**:
- `id`: Integer (Primary Key, Auto-increment)
- `email`: String (Required, Unique, max length 255)
- `created_at`: DateTime (Auto-generated on creation)
- `updated_at`: DateTime (Auto-generated on update)

**Validation Rules**:
- Email must be a valid email format
- Email must be unique across all users

**Relationships**:
- Has many Tasks (One-to-Many)

## State Transitions

**Task Completion**:
- A task can transition from `completed: false` to `completed: true`
- A task can transition from `completed: true` to `completed: false`
- No other state transitions are restricted beyond standard CRUD operations

## Database Constraints

- Foreign key constraint: `tasks.user_id` references `users.id`
- Index on `tasks.user_id` for efficient querying by user
- Unique constraint on `users.email`
- Index on `tasks.created_at` for chronological sorting