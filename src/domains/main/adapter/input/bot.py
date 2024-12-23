from unittest.mock import Mock

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from domains.main.application.port.input.family_manager import FamilyManagerInterface
from domains.main.application.port.input.user_manager import UserManagerInterface
from domains.main.adapter.input.fsm_create_family.create_family import create_family_router


class TaskBot:
    def __init__(self, bot_token, user_manager: UserManagerInterface, family_manager: FamilyManagerInterface):
        self.dispatcher: Dispatcher = Dispatcher(family_manager=family_manager)
        self.bot = Bot(token=bot_token, parse_mode=ParseMode.HTML)
        self.task_manager = Mock()
        # self.user_manager = user_manager
        # self.family_manager = family_manager
        self._register_routers()

    def _register_routers(self):
        self.dispatcher.include_router(create_family_router)

    async def _command_start_handler(self, message: Message) -> None:
        """Process the /start command"""
        hello_message = (f"Привет, {message.from_user.first_name}! Я бот для управления задачами. "
                         f"Для того чтобы зарегистрировать новую семью и стать ее админом, введи команду /new_family")
        await message.answer(hello_message)

    def _build_task_keyboard(self, task_ids: list) -> ReplyKeyboardBuilder:
        builder = ReplyKeyboardBuilder()
        for task_id in task_ids:
            builder.button(text=task_id)
        return builder

    async def _command_get_tasks_handler(self, message: Message) -> None:
        """
        Process the /task_list command.
        Should return the list of tasks with inline keyboard.
        """
        list_of_tasks = await self.task_manager.get_tasks_by_status(status='new')
        formatted_tasks_list = self.format_list_of_task(list_of_tasks)
        keyboard = self._build_task_keyboard(list_of_tasks.keys())
        await message.answer("\n".join(formatted_tasks_list), reply_markup=keyboard.as_markup())

    async def _command_choose_task_handler(self, message: Message):
        """
        Process the incoming message with the task_id
        :param message:
        :return:
        """
        task_id = message.text
        first_name = message.from_user.first_name
        user_id = message.from_user.id
        task_info = await self.task_manager.get_task_by_id(task_id=task_id)
        task_description = task_info.get('description')
        # TODO: вынести текст сообщения в конфиг
        await message.answer(f'Отлично! Задача {task_description} была зарегистрирована за пользователем {first_name}',
                             reply_markup=ReplyKeyboardRemove())
        # TODO: продумать логику по проверке назначения задания, напирмер если у пользователя уже есть задача
        assigned = await self.user_manager.assign_task(user_id=user_id, task_id=task_id)

    # async def _command_new_family_handler(self, message: Message):
    #     """
    #     Process the /new_family command
    #     """
    #     family_name = message.text
    #     family_id = await self.family_manager.create_family(family_name=family_name, user_id=message.from_user)
    #     await message.answer(f'Семья {family_name} была успешно создана. ID семьи: {family_id}')

    async def start_polling(self):
        # self.dispatcher.message.register(self._command_start_handler, CommandStart())
        # self.dispatcher.message.register(self._command_get_tasks_handler, Command('task_list'))
        # self.dispatcher.message.register(self._command_new_family_handler, Command('new_family'))
        # self.dispatcher.message.register(self._command_choose_task_handler)
        await self.dispatcher.start_polling(self.bot)

    def format_list_of_task(self, list_of_tasks: dict) -> list:
        """
        Format raw list of the tasks into HTML for TG.
        :param list_of_tasks:
        :return:

        <strong>Описание</strong>: бла бла бла
        <strong>Срок исполнения</strong>:
        <strong>Стоимость</strong>:

        """
        formatted_tasks_list = []
        for task_id, task_info in list_of_tasks.items():
            description = task_info['description']
            cost = task_info['cost']
            expiration_date = task_info['expiration_date']
            formatted_tasks_list.append(f"<strong>Описание</strong>: {description}\n"
                                        f"<strong>Срок иполнения</strong>: {expiration_date}\n"
                                        f"<strong>Стоимость</strong>: {cost}\n\n")
        return formatted_tasks_list
