from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.db import SessionLocal
from app.core.db_class import PostFeedback
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
    def get_feedback(post_id: int, db: Session):
        try:
            feedback = db.query(PostFeedback).filter(PostFeedback.post_id == post_id).first()
            if feedback is None:
                raise HTTPException(status_code=404, detail="Feedback not found")
            return feedback
        except HTTPException as http_exc:
            raise http_exc
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    @staticmethod
    def save_feedback(request: dto.PostFeedbackCreate, db: Session):
        try:
            db_feedback = PostFeedback(
                feedback=request.feedback,
                post_id=request.post_id,
                created_at=request.created_at,
                updated_at=request.updated_at
            )
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
