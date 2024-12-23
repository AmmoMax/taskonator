from pydantic import BaseModel
from typing import Optional
from enum import Enum
from uuid import UUID


class TaskStatus(str, Enum):
    NEW = 'new'
    ASSIGNED = 'assigned'
    COMPLETED = 'completed'
    VALIDATED = 'validated'


class Task(BaseModel):
    id: UUID
    description: str
    family_id: UUID
    status: TaskStatus = TaskStatus.NEW
    assigned_to: Optional[UUID] = None
