from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    study_tasks = relationship("StudyTask", back_populates="owner")

class StudyTask(Base):
    __tablename__ = "study_schedules"
    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String, index=True)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    is_completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="study_tasks")

# Pydantic models for API
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    is_active: bool = True
    items: List[StudyTask] = []

    class Config:
        orm_mode = True

class StudyTaskBase(BaseModel):
    task_name: str
    start_time: datetime
    end_time: datetime

class StudyTaskCreate(StudyTaskBase):
    pass

class StudyTask(StudyTaskBase):
    id: int
    user_id: int
    is_completed: bool

    class Config:
        orm_mode = True

