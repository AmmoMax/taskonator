from abc import ABC, abstractmethod

from src.domains.main.domain.user import User


class UserRepositoryPort(ABC):
    @abstractmethod
    async def create_user(self, user: User) -> None:
        raise NotImplementedError

    @abstractmethod
    async def get_user(self, user_id: str) -> User:
        raise NotImplementedError
