from pydantic import BaseModel, Field, ConfigDict
# from uuid import UUID, uuid4
from typing import Optional

class Base(BaseModel):
    message: Optional[str] = None
    err: Optional[str] = None

class Comment(Base):
    id: str
    comment: str

    model_config = ConfigDict(from_attributes=True)

class CommentGetResponse():
    comments: list[Comment]