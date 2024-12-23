from unittest.mock import Mock

from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer

from domains.main.adapter.output.family_repository_sql import FamilyRepositorySQL
from domains.main.application.service.family_management import FamilyManager
from domains.main.application.service.user_management import UserManager


class Container(DeclarativeContainer):
    task_repository = providers.Factory(Mock())
    user_repository = providers.Factory(Mock())
    user_manager = providers.Factory(UserManager,
                                     task_repository=task_repository,
                                     user_repository=user_repository)
    family_repository = providers.Factory(FamilyRepositorySQL)
    family_manager = providers.Factory(FamilyManager,
                                       family_repository=family_repository)
