"""
Configuration module for the Todo Backend API
This file consolidates all configuration settings for the backend application.
"""

import os
from typing import List
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration class to store all backend settings"""

    # App settings
    APP_NAME = os.getenv("APP_NAME", "Todo Backend API")
    VERSION = os.getenv("VERSION", "1.0.0")
    API_V1_PREFIX = os.getenv("API_V1_PREFIX", "/api/v1")

    # Database settings
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./todo_app.db")

    # Auth settings
    BETTER_AUTH_SECRET = os.getenv("BETTER_AUTH_SECRET", "your-test-secret-change-in-production")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

    # Server settings
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))

    # CORS settings
    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost,http://localhost:3000").split(",")

    # Logging
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    @classmethod
    def validate_config(cls):
        """Validate that required configuration values are present"""
        if not cls.BETTER_AUTH_SECRET or cls.BETTER_AUTH_SECRET == "your-test-secret-change-in-production":
            print("WARNING: Using default auth secret. Change this in production!")

        if "postgres" in cls.DATABASE_URL and "password" not in cls.DATABASE_URL:
            print("WARNING: Database URL may be missing credentials")

        return True

# Initialize configuration
config = Config()
config.validate_config()