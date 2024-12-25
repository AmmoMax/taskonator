from unittest.mock import Mock

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message

from domains.main.adapter.input.tg_handlers.tasks.tasks import tasks_router
from domains.main.application.port.input.family_manager import FamilyManagerInterface
from domains.main.application.port.input.task_manager import TaskManagerInterface
from domains.main.application.port.input.user_manager import UserManagerInterface
from domains.main.adapter.input.tg_handlers.family.create_family import create_family_router


class TaskBot:
    def __init__(self, bot_token, user_manager: UserManagerInterface, family_manager: FamilyManagerInterface, task_manager: TaskManagerInterface):
        self.dispatcher: Dispatcher = Dispatcher(family_manager=family_manager, user_manager=user_manager, task_manager=task_manager)
        self.bot = Bot(token=bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        self.task_manager = Mock()
        self._register_routers()

    def _register_routers(self):
        self.dispatcher.include_router(create_family_router)
        self.dispatcher.include_router(tasks_router)

    async def _command_start_handler(self, message: Message) -> None:
        """Process the /start command"""
        hello_message = (f"Привет, {message.from_user.first_name}! Я бот для управления задачами. "
                         f"Для того чтобы зарегистрировать новую семью и стать ее админом, введи команду /new_family")
        await message.answer(hello_message)


    async def start_polling(self):
        # self.dispatcher.message.register(self._command_start_handler, CommandStart())
        # self.dispatcher.message.register(self._command_get_tasks_handler, Command('task_list'))
        # self.dispatcher.message.register(self._command_new_family_handler, Command('new_family'))
        # self.dispatcher.message.register(self._command_choose_task_handler)
        await self.dispatcher.start_polling(self.bot)
