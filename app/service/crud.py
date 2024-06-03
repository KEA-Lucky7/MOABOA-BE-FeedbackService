from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.db import SessionLocal
from app.model.domain import entity
from app.model.dto import dto
from app.service import gpt_prompt


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class FeedbackService:
    @staticmethod
    def get_feedback(i: int, db: Session):
        try:
            feedbacks = db.query(entity.PostFeedback).offset(i).limit(1).all()
            return feedbacks
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def save_feedback(feedback: dto.PostFeedbackCreate, db: Session):
        try:
            db_feedback = entity.PostFeedback(feedback)
            db.add(db_feedback)
            db.commit()
            db.refresh(db_feedback)
            return db_feedback
        except Exception as e:
            db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

    @staticmethod
    def create_feedback(consumptions: dto.UserConsumptions):
        return gpt_prompt.create_feedback(consumptions)
