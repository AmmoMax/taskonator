from uuid import UUID

from domains.main.application.port.output.user_repository import UserRepositoryPort
from domains.main.domain.user import User, Role


class UserRepositorySQL(UserRepositoryPort):
    async def get_user(self, user_id: str) -> User:
        user_id = UUID('10000000-0000-0000-0000-000000000000')
        family_id = UUID('00000000-0000-0000-0000-000000000001')
        user = User(id=user_id,
                    telegram_id='1',
                    username='test',
                    role=Role.ADMIN,
                    family_id=family_id,
                    )
        return user

    async def create_user(self, user):
        pass
