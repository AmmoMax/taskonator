from pydantic import BaseModel, Field
from enum import Enum
from uuid import UUID, uuid4


class Role(str, Enum):
    ADMIN = 'admin'
    USER = 'user'


class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    telegram_id: int
    username: str
    role: Role
    family_id: UUID
    points: int = 0
