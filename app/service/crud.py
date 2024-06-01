from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.db import SessionLocal
from app.model.dao import dao
from app.model.domain import entity


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class FeedbackService:
    @staticmethod
    def get_feedback(db: Session, i: int):
        try:
            feedbacks = db.query(entity.PostFeedback).offset(i).limit(1).all()
            return feedbacks
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_feedback(db: Session, feedback: dao.PostFeedbackCreate):
        try:
            db_feedback = entity.PostFeedback(feedback=feedback.feedback)
            db.add(db_feedback)
            db.commit()
            db.refresh(db_feedback)
            return db_feedback
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
