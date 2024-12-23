import asyncio
from os import getenv

from aiogram import Dispatcher
from dependency_injector.wiring import inject, Provide
from domains.command.main.bot_app.container import Container
from domains.main.adapter.input.fsm_create_family.create_family import create_family_router
from src.domains.main.adapter.input.bot import TaskBot
from domains.main.application.service.user_management import UserManager
from domains.main.application.service.family_management import FamilyManager


@inject
async def run_bot(user_manager: UserManager = Provide[Container.user_manager],
                  family_manager: FamilyManager = Provide[Container.family_manager]):
    # TODO: вынести в конфиг
    BOT_TOKEN = getenv("BOT_TOKEN")

    bot = TaskBot(bot_token=BOT_TOKEN,
                  user_manager=user_manager,
                  family_manager=family_manager)

    await bot.start_polling()


if __name__ == '__main__':
    container = Container()
    container.init_resources()

    container.wire(modules=[__name__])

    asyncio.run(run_bot())
