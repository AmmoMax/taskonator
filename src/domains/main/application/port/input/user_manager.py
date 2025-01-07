from abc import ABC, abstractmethod

from domains.main.domain.user import User


class UserManagerInterface(ABC):
    @abstractmethod
    async def create_user(self, username: str, user_id: str):
        raise NotImplementedError

    @abstractmethod
    async def assign_task(self, user_id: str, task_id: str) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def get_user(self, tg_user_id: int) -> User:
        raise NotImplementedError
