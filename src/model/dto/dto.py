from pydantic import BaseModel, Field
from typing import List
from datetime import date, datetime

from sqlalchemy import Column, DateTime
from sqlalchemy.ext.declarative import as_declarative


@as_declarative()
class Base:
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    __name__: str


class ConsumptionHistory(BaseModel):
    name: str
    category: str
    cost: int
    date: date


class UserConsumptions(BaseModel):
    post_id: int
    consumption_history: List[ConsumptionHistory]


class PostFeedbackBase(BaseModel):
    post_id: int
    feedback: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Config:
        orm_mode = True


class PostFeedbackCreate(PostFeedbackBase):
    pass


class PostFeedbackVO(BaseModel):
    id: int
    post_id: int
    feedback: str

    class Config:
        from_attributes = True


class PostFeedbackRead(BaseModel):
    id: int
    post_id: int
    feedback: str
