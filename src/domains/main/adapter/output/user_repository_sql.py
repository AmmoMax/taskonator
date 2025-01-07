from uuid import UUID

from sqlalchemy import select

from domains.main.adapter.output.db_models import DBUser
from domains.main.application.port.output.user_repository import UserRepositoryPort
from domains.main.domain.user import User, Role


class UserRepositorySQL(UserRepositoryPort):
    def __init__(self, session):
        self._session = session

    async def get_user(self, user_id: str) -> User | None:
        async with self._session() as session:
            stmt = select(DBUser).where(DBUser.tg_id == user_id)
            result = await session.execute(stmt)
            if not result:
                return None
            user = result.scalars().one_or_none()
        return user

    async def create_user(self, user):
        pass
