# Cognate Backend (FastAPI)
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from . import models, database

app = FastAPI(
    title="Cognate API",
    description="AI-powered personalized learning ecosystem.",
    version="1.0.0",
)

# Create database tables on startup
@app.on_event("startup")
def create_db_and_tables():
    database.Base.metadata.create_all(bind=database.engine)

# Dependency to get a DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Welcome to the Cognate FastAPI Backend!"}

# --- User Management ---
@app.post("/users/", response_model=models.User, tags=["Users"])
def create_user(user: models.UserCreate, db: Session = Depends(get_db)):
    # In a real app, you would hash the password
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/", response_model=List[models.User], tags=["Users"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

# --- Study Scheduling ---
@app.post("/study-tasks/", response_model=models.StudyTask, tags=["Study"])
def create_study_task(task: models.StudyTask, db: Session = Depends(get_db)):
    db_task = models.StudyTask(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

# --- AI-Powered Features (Placeholders) ---
@app.post("/ai/adaptive-schedule/", tags=["AI"])
def get_adaptive_schedule(user_id: int):
    # TODO: Implement GPT-4 logic for adaptive scheduling
    return {"message": f"Adaptive schedule for user {user_id} would be generated here."}

@app.post("/ai/career-coach/", tags=["AI"])
def get_career_advice(user_id: int):
    # TODO: Implement career coaching logic using real-time job data
    return {"message": f"Career advice for user {user_id} would be generated here."}

