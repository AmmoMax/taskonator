from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class Family(BaseModel):
    id: UUID
    name: str
