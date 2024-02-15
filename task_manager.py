from typing import Protocol

from task_store import PTaskStore


class PTaskManager(Protocol):
    async def get_tasks_by_status(self, status: str) -> list:
        pass

    async def change_task_status(self, task_id: str, status: str):
        pass


class TaskManager:
    def __init__(self, task_store: PTaskStore):
        self._task_store = task_store

    async def get_tasks_by_status(self, status):
        tasks = self._task_store.get_task_by_status(status)
        return tasks
