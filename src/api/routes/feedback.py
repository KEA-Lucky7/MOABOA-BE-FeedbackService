from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.service.crud import FeedbackService, get_db
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
def save_feedback(consumptions: dto.UserConsumptions, db: Session = Depends(get_db)):
    try:
        if is_feedback_present(db, consumptions):
            return update_feedback(consumptions, db)
        else:
            return create_feedback(consumptions, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


def create_feedback(consumptions, db):
    feedback = FeedbackService.create_feedback(consumptions)
    post_feedback_create = dto.PostFeedbackCreate(post_id=consumptions.post_id, feedback=feedback)

    # 피드백 저장
    return FeedbackService.save_feedback(db=db, request=post_feedback_create)


def update_feedback(consumptions, db):
    feedback = FeedbackService.create_feedback(consumptions)
    post_feedback_update = dto.PostFeedbackUpdate(post_id=consumptions.post_id, feedback=feedback)
    return FeedbackService.update_feedback(db=db, request=post_feedback_update)


def is_feedback_present(db: Session, consumptions: dto.UserConsumptions):
    existing_feedback = db.query(PostFeedback).filter(PostFeedback.post_id == consumptions.post_id).first()
    if existing_feedback is not None:
        return True
    else:
        return False
