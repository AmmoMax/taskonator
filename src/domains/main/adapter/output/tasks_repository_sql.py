import uuid
from datetime import datetime
from uuid import UUID

from domains.main.application.port.output.task_repository import TaskRepositoryPort
from domains.main.domain.task import Task, TaskStatus


class TaskRepositorySQL(TaskRepositoryPort):
    async def update_task_status(self, task_id: str, status: str):
        pass

    async def get_available_tasks(self, family_id: UUID) -> list[Task]:
        tasks = [
            Task(
                id=uuid.uuid4(),
                description="Task 1 description",
                family_id=family_id,
                status=TaskStatus.NEW,
                expiration_date=datetime(year=2025, month=1, day=21),
                cost=10
            ),
            Task(
                id=uuid.uuid4(),
                description="Task 2 description",
                family_id=family_id,
                status=TaskStatus.NEW,
                expiration_date=datetime(year=2025, month=1, day=21),
                cost=10
            ),
            Task(
                id=uuid.uuid4(),
                description="Task 3 description",
                family_id=family_id,
                status=TaskStatus.NEW,
                expiration_date=datetime(year=2025, month=1, day=21),
                cost=2
            )
        ]
        return tasks

    async def get_by_id(self, task_id: int):
        pass

    async def save(self, task: Task):
        pass