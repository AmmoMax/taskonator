from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from uuid import UUID, uuid4


class TaskStatus(str, Enum):
    NEW = 'new'
    ASSIGNED = 'assigned'
    COMPLETED = 'completed'
    VALIDATED = 'validated'


class Task(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    description: str
    family_id: UUID
    status: TaskStatus = TaskStatus.NEW
    assigned_to: Optional[UUID] = None
    submission_id: Optional[UUID] = None
