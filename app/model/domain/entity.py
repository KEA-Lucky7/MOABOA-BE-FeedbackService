from sqlalchemy import Column, Integer, String, DateTime, func

from app.core.db import Base


class PostFeedback(Base):
    __tablename__ = "post_feedback"

    id = Column(Integer, primary_key=True)
    feedback = Column(String)
    post_id = Column(Integer)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

