from abc import ABC, abstractmethod

from src.domains.main.domain.task import Task


class TaskRepositoryPort(ABC):
    @abstractmethod
    async def get_by_id(self, task_id: int):
        raise NotImplementedError

    @abstractmethod
    async def save(self, task: Task):
        raise NotImplementedError

    @abstractmethod
    async def update_task_status(self, task_id: str, status: str):
        raise NotImplementedError

    @abstractmethod
    async def get_available_tasks(self, family_id: str) -> list[Task]:
        raise NotImplementedError
