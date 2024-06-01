from pydantic import BaseModel


class PostFeedbackBase(BaseModel):
    feedback: str


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