from domains.main.application.port.output.task_repository import TaskRepositoryPort
from domains.main.domain.task import Task


class TaskRepositorySQL(TaskRepositoryPort):
    async def update_task_status(self, task_id: str, status: str):
        pass

    async def get_available_tasks(self, family_id: str) -> list[Task]:
        pass

    async def get_by_id(self, task_id: int):
        pass

    async def save(self, task: Task):
        pass