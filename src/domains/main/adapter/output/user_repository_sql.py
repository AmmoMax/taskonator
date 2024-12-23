from domains.main.application.port.output.user_repository import UserRepositoryPort
from domains.main.domain.user import User


class UserRepositorySQL(UserRepositoryPort):
    async def get_user(self, user_id: str) -> User:
        pass

    async def create_user(self, user):
        pass
