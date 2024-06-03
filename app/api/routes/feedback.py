from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.service.crud import FeedbackService, get_db
from ...core.db_class import PostFeedback
from ...model.dto import dto

feedbackRouter = APIRouter()

@feedbackRouter.get("", response_model=dto.PostFeedbackRead)
def read_feedback(post_id: int, db: Session = Depends(get_db)):
    try:
        feedbacks = FeedbackService.get_feedback(db=db, post_id=post_id)
        return feedbacks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@feedbackRouter.post("", response_model=dto.PostFeedbackRead)
def create_feedback(consumptions: dto.UserConsumptions, db: Session = Depends(get_db)):
    try:
        existing_feedback = db.query(PostFeedback).filter(PostFeedback.post_id == consumptions.post_id).first()
        if existing_feedback:
            raise HTTPException(status_code=400, detail="Feedback for this post already exists")

        # 피드백 생성
        feedback = FeedbackService.create_feedback(consumptions)
        post_feedback_create = dto.PostFeedbackCreate(post_id=consumptions.post_id, feedback=feedback)

        # 피드백 저장
        return FeedbackService.save_feedback(db=db, request=post_feedback_create)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
