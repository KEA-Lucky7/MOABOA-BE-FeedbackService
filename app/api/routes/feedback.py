from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.service.crud import FeedbackService, get_db
from ...model.dao import dao

feedbackRouter = APIRouter()

db: Session = Depends(get_db)

@feedbackRouter.get("/feedback", response_model=dao.PostFeedbackRead)
def read_feedback(request: str):
    try:
        feedbacks = FeedbackService.get_feedback(db=db)
        return feedbacks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@feedbackRouter.post("/feedback", response_model=dao.PostFeedbackRead)
def create_feedback(feedback: dao.PostFeedbackCreate):
    try:
        return FeedbackService.create_feedback(db=db, feedback=feedback)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
