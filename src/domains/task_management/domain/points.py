from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class Points(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    user_id: UUID
    task_id: UUID
    points: int
