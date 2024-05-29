from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from app.core.db import Base


class PostFeedback(Base):
    __tablename__ = "post_feedback"

    id = Column(Integer, primary_key=True)
    feedback = Column(String)
    post_id = Column(Integer)