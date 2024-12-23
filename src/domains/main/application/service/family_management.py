from uuid import uuid4

from domains.main.application.port.input.family_manager import FamilyManagerInterface
from domains.main.application.port.output.family_repository import FamilyRepositoryPort
from domains.main.domain.family import Family
from domains.main.domain.user import User


class FamilyManager(FamilyManagerInterface):
    def __init__(self, family_repository: FamilyRepositoryPort):
        self.family_repository = family_repository


    async def create_family(self, family_name: str, user_id: str) -> Family:
        """
        Create a new family and defines the current user as the family admin.
        """
        print('creating new family...')
        new_family = Family(id=uuid4(), name=family_name)
        await self.family_repository.create_family(new_family, user_id)
        print('new family was successfully created!')
        return new_family

    async def add_new_member(self, user_info: dict, family_id: str) -> None:
        pass
