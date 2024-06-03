from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.service.crud import FeedbackService, get_db
from ...model.dto import dto

feedbackRouter = APIRouter()


@feedbackRouter.get("", response_model=dto.PostFeedbackRead)
def read_feedback(request: str, db: Session = Depends(get_db)):
    try:
        feedbacks = FeedbackService.get_feedback(db=db)
        return feedbacks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@feedbackRouter.post("", response_model=dto.PostFeedbackRead)
def create_feedback(consumptions: dto.UserConsumptions, db: Session = Depends(get_db)):
    try:
        # 피드백 생성
        feedback = FeedbackService.create_feedback(consumptions)
        post_feedback_create = dto.PostFeedbackCreate(post_id=consumptions.post_id, feedback=feedback)

        # 피드백 저장
        return FeedbackService.save_feedback(db=db, feedback=post_feedback_create)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
