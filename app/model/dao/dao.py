from pydantic import BaseModel


class PostFeedbackBase(BaseModel):
    feedback: str


class PostFeedbackCreate(PostFeedbackBase):
    pass


class PostFeedback(PostFeedbackBase):
    id: int
    post_id: int

    class Config:
        orm_mode = True
