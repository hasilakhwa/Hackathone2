"""
Start script for the Todo Backend API
This script provides a proper entry point for running the backend server.
"""

import uvicorn
import sys
import os

# Add the src directory to the path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))

from src.main import app
from config import config


def start_server():
    """Start the FastAPI server with configured settings"""
    print(f"Starting {config.APP_NAME} v{config.VERSION}")
    print(f"Listening on {config.HOST}:{config.PORT}")
    print(f"API available at http://{config.HOST}:{config.PORT}{config.API_V1_PREFIX}")

    uvicorn.run(
        "src.main:app",
        host=config.HOST,
        port=config.PORT,
        reload=True,  # Set to False in production
        log_level=config.LOG_LEVEL.lower()
    )


if __name__ == "__main__":
    start_server()