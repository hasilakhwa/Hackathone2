from sqlmodel import create_engine, Session
from sqlalchemy import event
from sqlalchemy.pool import StaticPool, QueuePool
from typing import Generator
import os
from dotenv import load_dotenv

load_dotenv()

# Get database URL from environment, with a default for testing
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# For PostgreSQL/Neon, use psycopg2 driver for sync operations
if "postgresql" in DATABASE_URL:
    # Replace postgresql+asyncpg:// with postgresql+psycopg2:// for sync support
    if DATABASE_URL.startswith("postgresql+asyncpg://"):
        DATABASE_URL = DATABASE_URL.replace("postgresql+asyncpg://", "postgresql+psycopg2://", 1)
    elif DATABASE_URL.startswith("postgresql://"):
        DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+psycopg2://", 1)

# Create sync engine for standard operations
if DATABASE_URL.startswith("sqlite"):
    # For SQLite, use StaticPool
    sync_engine = create_engine(
        DATABASE_URL,
        echo=False,
        poolclass=StaticPool,
        connect_args={"check_same_thread": False}  # Required for SQLite
    )
else:
    # For PostgreSQL, use QueuePool
    sync_engine = create_engine(
        DATABASE_URL,
        echo=False,
        poolclass=QueuePool,
        pool_size=5,
        max_overflow=10,
        pool_pre_ping=True,
        pool_recycle=300
    )


def get_session() -> Generator[Session, None, None]:
    """Get a synchronous database session"""
    with Session(sync_engine) as session:
        yield session


# Optional: Add connection pooling configuration
@event.listens_for(sync_engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    """Set SQLite pragmas for better performance (only used in testing with SQLite)"""
    if dbapi_connection.__class__.__module__ == "sqlite3":
        cursor = dbapi_connection.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()


def init_db():
    """Initialize the database and create tables"""
    from sqlmodel import SQLModel
    from ..models.user import User  # noqa: F401
    from ..models.task import Task  # noqa: F401

    SQLModel.metadata.create_all(sync_engine)