import logging

from sqlalchemy.orm import Session

from domains.main.adapter.output.db_models import DBUser
from domains.main.application.port.output.family_repository import FamilyRepositoryPort
from domains.main.domain.family import Family
from domains.main.domain.user import User


class FamilyRepositorySQL(FamilyRepositoryPort):
    def __init__(self, session: Session):
        self._logger = logging.getLogger(__name__)
        self._session = session

    async def create_family(self, family: Family, user: User) -> None:
        pass