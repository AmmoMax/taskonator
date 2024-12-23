from domains.main.application.port.output.family_repository import FamilyRepositoryPort
from domains.main.domain.family import Family
from domains.main.domain.user import User


class FamilyRepositorySQL(FamilyRepositoryPort):
    async def create_family(self, family: Family, user_id: str) -> None:
        print(f'Creating family {family.name} for user {user_id}')