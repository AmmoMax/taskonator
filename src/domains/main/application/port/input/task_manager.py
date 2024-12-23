from abc import ABC, abstractmethod


class TaskManagerInterface(ABC):
    async def get_available_tasks(self, user_id: str) -> list:
        raise NotImplementedError

    async def change_task_status(self, task_id: str, status: str):
        raise NotImplementedError
