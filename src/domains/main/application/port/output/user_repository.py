from abc import ABC, abstractmethod

from src.domains.main.domain.user import User


class UserRepositoryPort(ABC):
    @abstractmethod
    async def create(self, user: User) -> None:
        raise NotImplementedError
