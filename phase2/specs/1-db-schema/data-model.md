# Data Model: Multi-User Todo Application

## Entity: User

### Fields:
- **id**: Integer, Primary Key, Auto-increment
- **email**: String, Unique, Required
- **created_at**: DateTime, Required, Default to current timestamp
- **updated_at**: DateTime, Required, Auto-updates to current timestamp

### Relationships:
- **tasks**: One-to-Many relationship to Task entity (back_populates: "user")

### Validation Rules:
- Email must be a valid email format
- Email must be unique across all users
- Email cannot be empty or null

## Entity: Task

### Fields:
- **id**: Integer, Primary Key, Auto-increment
- **title**: String, Required (max length 255)
- **description**: String, Optional (max length 1000)
- **completed**: Boolean, Required, Default False
- **created_at**: DateTime, Required, Default to current timestamp
- **updated_at**: DateTime, Required, Auto-updates to current timestamp
- **user_id**: Integer, Foreign Key referencing User.id, Required

### Relationships:
- **user**: Many-to-One relationship to User entity (back_populates: "tasks")

### Validation Rules:
- Title cannot be empty or null
- User must exist (foreign key constraint)
- Completed status defaults to False
- Description can be empty but not exceeding max length

## State Transitions:

### Task State Transitions:
- New Task: `completed = False`
- Mark Complete: `completed = True`
- Mark Incomplete: `completed = False`

## Database Constraints:

### Foreign Key Constraints:
- Task.user_id must reference an existing User.id
- ON DELETE CASCADE: When a User is deleted, all their Tasks are automatically deleted

### Indexes:
- Index on Task.user_id for efficient querying by user
- Unique constraint on User.email
- Index on User.created_at for sorting/filtering

## Access Control Rules:
- A Task can only be accessed/modified by the User who owns it (determined by user_id)
- Cross-user access is prohibited at the application layer
- Foreign key constraints enforce referential integrity at the database level