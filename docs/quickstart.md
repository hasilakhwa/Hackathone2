# Quickstart Guide: Phase I — In-Memory Python Console Todo App

## Prerequisites

- Python 3.13+
- `pip` package manager

## Setup

1. **Install dependencies**:
   ```bash
   pip install -e .
   ```

2. **Run the application**:
   ```bash
   python -m src.todo_app.main
   ```

   Or if installed as a package:
   ```bash
   todo-app
   ```

## Using the Application

The application provides an interactive menu system:

1. **Add a new task**: Select option 1 and enter the task description
2. **View all tasks**: Select option 2 to see all tasks with their status
3. **Mark task as complete**: Select option 3 and enter the task ID
4. **Update task description**: Select option 4, enter task ID and new description
5. **Delete task**: Select option 5 and enter the task ID
6. **Exit**: Select option 6 to quit the application

## Testing

Run the full test suite:
```bash
python -m pytest tests/
```

Run specific test types:
```bash
# Unit tests
python -m pytest tests/unit/

# Integration tests
python -m pytest tests/integration/
```

## Project Structure

```
src/
├── todo_app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── task.py          # Task data model and in-memory storage
│   ├── services/
│   │   ├── __init__.py
│   │   └── task_service.py  # Business logic for task operations
│   ├── cli/
│   │   ├── __init__.py
│   │   └── cli.py           # Command-line interface and menu system
│   └── main.py              # Application entry point
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── __init__.py
│   │   ├── test_task_model.py
│   │   ├── test_task_service.py
│   │   └── test_error_handling.py
│   ├── integration/
│   │   ├── __init__.py
│   │   ├── test_add_task.py
│   │   ├── test_view_tasks.py
│   │   ├── test_mark_complete.py
│   │   ├── test_update_task.py
│   │   └── test_delete_task.py
│   └── conftest.py
├── pyproject.toml
└── README.md
```

## Development

To add new functionality:
1. Update the appropriate layer (models, services, or cli)
2. Write corresponding unit tests
3. Run tests to ensure functionality works as expected
4. Follow the separation of concerns principle