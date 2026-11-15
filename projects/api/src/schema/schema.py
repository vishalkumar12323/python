from pydantic import BaseModel, ConfigDict, Field
from typing import Optional


class Base(BaseModel):
    message: Optional[str] = None
    err: Optional[str] = None


class Comment(Base):
    id: str
    comment: str

    model_config = ConfigDict(from_attributes=True)


class CommentCreate(BaseModel):
    comment: str = Field(min_length=1, max_length=10_000)


class CommentUpdate(BaseModel):
    comment: str = Field(min_length=1, max_length=10_000)


class CommentGetResponse(Base):
    comments: list[Comment]