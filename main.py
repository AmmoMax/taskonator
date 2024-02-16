import asyncio
from os import getenv
from datetime import date

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from models import User
from task_manager import TaskManager
from task_store import TaskStore

# TODO: вынести в конфиг
BOT_TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()


class TaskBot:
    def __init__(self, bot_token, task_manager: TaskManager):
        self._bot_token = bot_token
        self.dispatcher = Dispatcher()
        self.bot = Bot(token=self._bot_token, parse_mode=ParseMode.HTML)
        self.task_manager = task_manager

    async def _command_start_handler(self, message: Message) -> None:
        """Process the /start command"""
        user = User(telegram_id=message.from_user.id,
                    username=message.from_user.username,
                    first_name=message.from_user.first_name)
        print(user)

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
        task_info = await self.task_manager.get_task_by_id(task_id=task_id)
        task_description = task_info.get('description')
        await message.answer(f'Отлично! Задача {task_description} была зарегистрирована за пользователем {first_name}',
                             reply_markup=ReplyKeyboardRemove())

    async def start_polling(self):
        self.dispatcher.message.register(self._command_start_handler, CommandStart())
        self.dispatcher.message.register(self._command_get_tasks_handler, Command('task_list'))
        self.dispatcher.message.register(self._command_choose_task_handler)
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


async def main() -> None:
    task_store = TaskStore()
    await task_store.create_task(description="Clean the toilet",
                                 cost='100',
                                 expiration_date=date(year=2024, month=2, day=20),
                                 status='new')  # TODO: вынести в конфиг статус

    await task_store.create_task(description="Mow the lawn",
                                 cost='221',
                                 expiration_date=date(year=2024, month=3, day=1),
                                 status='new')  # TODO: вынести в конфиг статус

    task_manager = TaskManager(task_store=task_store)

    bot = TaskBot(bot_token=BOT_TOKEN, task_manager=task_manager)
    await bot.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
