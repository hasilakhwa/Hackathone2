# Data Model: Phase I — In-Memory Python Console Todo App

**Date**: 2026-01-02
**Feature**: 001-todo-app
**Status**: Complete

## Entities

### Task

**Description**: Represents a single todo item in the application

**Fields**:
- `id` (int): Unique identifier for the task (auto-incremented)
- `description` (str): Text description of the task
- `completed` (bool): Status indicating if the task is completed (default: False)
- `created_at` (datetime): Timestamp when the task was created

**Validation Rules**:
- `id` must be a positive integer
- `description` must not be empty or None
- `description` must be less than 1000 characters
- `completed` must be a boolean value
- `created_at` must be a valid datetime object

**State Transitions**:
- Initial state: `completed = False`
- Transition to complete: `completed = True` (via mark_complete operation)
- No transition back to incomplete (as per requirements)

**Relationships**:
- None (standalone entity)

### TaskList

**Description**: Collection of Task entities stored in memory

**Fields**:
- `tasks` (list): List of Task objects
- `next_id` (int): Counter for generating next unique ID

**Operations**:
- Add task to list
- Remove task from list by ID
- Update task in list by ID
- Retrieve all tasks
- Find task by ID

## Data Storage

**In-Memory Storage**: All tasks are stored in a Python list during application runtime
- No persistence between application runs
- Simple data structure for fast access
- Memory efficient for small to medium task lists

## API Contracts

### Task Creation
- Input: description (str)
- Output: Task object with assigned ID and default status
- Validation: Description must be non-empty

### Task Retrieval
- Input: None (for all tasks) or task_id (int)
- Output: Task object or list of Task objects
- Validation: ID must exist in the list

### Task Update
- Input: task_id (int), updated description (str) or completion status
- Output: Updated Task object
- Validation: ID must exist, description must be valid

### Task Deletion
- Input: task_id (int)
- Output: Boolean indicating success
- Validation: ID must exist in the list

## Constraints

1. **Uniqueness**: Each Task must have a unique ID
2. **Integrity**: Task descriptions must not be empty
3. **Completeness**: All required fields must be present
4. **Immutability**: Once created, Task ID cannot be changed
5. **Runtime Scope**: Data only persists during application execution