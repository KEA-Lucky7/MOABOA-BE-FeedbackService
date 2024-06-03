from sqlalchemy import Column, Integer, DateTime, VARCHAR

from app.core.db import Base


class PostFeedback(Base):
    __tablename__ = 'post_feedback'

    id = Column(Integer, primary_key=True, autoincrement=True)
    feedback = Column(VARCHAR(255), nullable=False)
    post_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)