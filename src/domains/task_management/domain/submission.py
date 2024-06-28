from pydantic import BaseModel, Field, HttpUrl
from typing import List
from uuid import UUID, uuid4


class Submission(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    task_id: UUID
    user_id: UUID
    media_urls: List[HttpUrl]
