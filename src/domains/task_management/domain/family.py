from pydantic import BaseModel, Field
from typing import List
from uuid import UUID, uuid4


class Family(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    members: List[UUID] = []
