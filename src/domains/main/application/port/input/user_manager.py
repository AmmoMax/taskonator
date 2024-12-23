from abc import ABC, abstractmethod


class UserManagerInterface(ABC):
    @abstractmethod
    async def create_user(self, username: str, user_id: str):
        raise NotImplementedError

    @abstractmethod
    async def assign_task(self, user_id: str, task_id: str) -> bool:
        raise NotImplementedError