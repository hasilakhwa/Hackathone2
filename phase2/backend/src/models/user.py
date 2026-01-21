from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
from .task import Task


class UserBase(SQLModel):
    email: str = Field(unique=True, nullable=False, max_length=255)


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})

    # Relationship to tasks
    tasks: List[Task] = Relationship(back_populates="user")


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime