from src.todo_app.services.task_service import TaskService
from src.todo_app.cli.cli import TodoCLI


def main():
    """
    Main entry point for the todo application
    """
    # Initialize the task service
    task_service = TaskService()

    # Initialize the CLI interface
    cli = TodoCLI(task_service)

    # Run the application
    cli.run()


if __name__ == "__main__":
    main()