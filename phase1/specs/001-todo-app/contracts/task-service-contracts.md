# API Contracts: Phase I — In-Memory Python Console Todo App

## Task Service Contracts

### Add Task
- **Method**: `add_task(description: str)`
- **Input**: Task description (string)
- **Output**: Task object with ID, description, completed status, and creation timestamp
- **Validation**: Description must not be empty
- **Error cases**: ValueError if description is empty

### Get All Tasks
- **Method**: `get_all_tasks()`
- **Input**: None
- **Output**: List of Task objects
- **Validation**: None
- **Error cases**: None

### Get Task by ID
- **Method**: `get_task(task_id: int)`
- **Input**: Task ID (integer)
- **Output**: Task object
- **Validation**: Task ID must exist
- **Error cases**: ValueError if task ID doesn't exist

### Update Task
- **Method**: `update_task(task_id: int, description: str)`
- **Input**: Task ID (integer), new description (string)
- **Output**: Updated Task object
- **Validation**: Task ID must exist, description must not be empty
- **Error cases**: ValueError if task ID doesn't exist or description is empty

### Mark Task Complete
- **Method**: `mark_task_complete(task_id: int)`
- **Input**: Task ID (integer)
- **Output**: Updated Task object
- **Validation**: Task ID must exist
- **Error cases**: ValueError if task ID doesn't exist

### Delete Task
- **Method**: `delete_task(task_id: int)`
- **Input**: Task ID (integer)
- **Output**: Boolean indicating success
- **Validation**: Task ID must exist
- **Error cases**: ValueError if task ID doesn't exist