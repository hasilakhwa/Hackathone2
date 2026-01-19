# Quickstart Guide: Phase I — In-Memory Python Console Todo App

**Date**: 2026-01-02
**Feature**: 001-todo-app

## Prerequisites

- Python 3.13+
- `uv` package manager

## Setup

1. **Install dependencies**:
   ```bash
   uv sync
   ```

2. **Install the package in development mode**:
   ```bash
   uv build
   ```

## Running the Application

1. **Start the application**:
   ```bash
   python -m src.todo_app.main
   ```

   Or if installed as a package:
   ```bash
   python -c "from src.todo_app.main import main; main()"
   ```

## Using the Application

The application provides an interactive menu system:

1. **Add a new task**: Select option 1 and enter the task description
2. **View all tasks**: Select option 2 to see all tasks with their status
3. **Update a task**: Select option 3, enter task ID and new description
4. **Delete a task**: Select option 4 and enter the task ID
5. **Mark task as complete**: Select option 5 and enter the task ID
6. **Exit**: Select option 6 to quit the application

## Testing

Run the full test suite:
```bash
uv run pytest
```

Run specific test types:
```bash
# Unit tests
uv run pytest tests/unit/

# Integration tests
uv run pytest tests/integration/
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
│   │   └── test_task_service.py
│   ├── integration/
│   │   ├── __init__.py
│   │   └── test_cli_integration.py
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