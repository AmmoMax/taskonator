from abc import ABC, abstractmethod

from domains.main.domain.user import User
from src.domains.main.domain.family import Family


class FamilyRepositoryPort(ABC):

    @abstractmethod
    async def create_family(self, family: Family, user_id: str) -> None:
        raise NotImplementedError
