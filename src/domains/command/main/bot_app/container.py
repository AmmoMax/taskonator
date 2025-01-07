from logging.config import dictConfig

from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app_logging.config import json_logger_config_factory
from domains.main.adapter.output.family_repository_sql import FamilyRepositorySQL
from domains.main.adapter.output.tasks_repository_sql import TaskRepositorySQL
from domains.main.adapter.output.user_repository_sql import UserRepositorySQL
from domains.main.application.service.family_management import FamilyManager
from domains.main.application.service.user_management import UserManager
from domains.main.application.service.task_management import TaskManager
from domains.command.configuration import Config, DBConfig

def init_db_session(db_config: DBConfig) -> async_sessionmaker[AsyncSession]:
    async_engine = create_async_engine(db_config.postgres_url)
    async_session = async_sessionmaker(async_engine)
    return async_session



class Container(DeclarativeContainer):
    config = Config()
    db_config = DBConfig()
    db_session = providers.Singleton(init_db_session, db_config=db_config)
    task_repository = providers.Factory(TaskRepositorySQL)
    user_repository = providers.Factory(UserRepositorySQL, session=db_session)
    user_manager = providers.Factory(UserManager,
                                     task_repository=task_repository,
                                     user_repository=user_repository)
    family_repository = providers.Factory(FamilyRepositorySQL, session=db_session)
    family_manager = providers.Factory(FamilyManager,
                                       family_repository=family_repository)
    task_manager = providers.Factory(TaskManager,
                                     task_repository=task_repository,
                                     user_repository=user_repository)
    logger = providers.Resource(dictConfig, json_logger_config_factory(config.LOGGING_LEVEL))
