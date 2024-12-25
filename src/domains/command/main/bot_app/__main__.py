import asyncio
import logging
from os import getenv

from dependency_injector.wiring import inject, Provide
from domains.command.main.bot_app.container import Container
from domains.main.application.service.task_management import TaskManager
from src.domains.main.adapter.input.bot import TaskBot
from domains.main.application.service.user_management import UserManager
from domains.main.application.service.family_management import FamilyManager

logger = logging.getLogger(__name__)


@inject
async def run_bot(user_manager: UserManager = Provide[Container.user_manager],
                  family_manager: FamilyManager = Provide[Container.family_manager],
                  task_manager: TaskManager=Provide[Container.task_manager]):
    # TODO: вынести в конфиг
    BOT_TOKEN = getenv("BOT_TOKEN")

    bot = TaskBot(bot_token=BOT_TOKEN,
                  user_manager=user_manager,
                  family_manager=family_manager,
                  task_manager=task_manager)

    logger.info('Bot was successfully started...')
    await bot.start_polling()


if __name__ == '__main__':
    container = Container()
    container.init_resources()

    container.wire(modules=[__name__])

    asyncio.run(run_bot())
