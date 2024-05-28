from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.service.crud import FeedbackService, get_db
from ...model.dao import dao
from ...model.domain import entity

feedbackRouter = APIRouter()


@feedbackRouter.get("/feedback", response_model = List[entity.PostFeedback])
def read_feedback(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        feedbacks = FeedbackService.get_feedback(db=db, skip=skip, limit=limit)
        return feedbacks
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@feedbackRouter.post("/feedback", response_model=entity.PostFeedback)
def create_feedback(feedback: dao.PostFeedbackCreate, db: Session = Depends(get_db)):
    try:
        return FeedbackService.create_feedback(db=db, feedback=feedback)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
