from abc import ABC, abstractmethod


class FamilyManagerInterface(ABC):
    @abstractmethod
    async def create_family(self, family_name: str, user_id: str) -> dict:
        raise NotImplementedError

    @abstractmethod
    async def add_new_member(self, user_info: dict, family_id: str) -> None:
        raise NotImplementedError
