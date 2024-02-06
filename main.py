import asyncio
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import CommandStart, Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from models import User

BOT_TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()

# TODO: черновой вариант списка задач. переделать на модель
list_of_tasks = {
    "task_id_1": {
        "description": "Clean the toilet",
        "cost": 100,
        "expiration_date": "2024-02-10"
    },
    "task_id_2": {
        "description": "Mow the lawn",
        "cost": 200,
        "expiration_date": "2024-02-11"
    }
}


class TaskBot:
    def __init__(self, bot_token):
        self._bot_token = bot_token
        self.dispatcher = Dispatcher()
        self.bot = Bot(token=self._bot_token, parse_mode=ParseMode.HTML)

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
        tasks_list = []
        for task in list_of_tasks.values():
            tasks_list.append(task)
        keyboard = self._build_task_keyboard(list_of_tasks.keys())
        await message.answer(f"List of tasks: {tasks_list}", reply_markup=keyboard.as_markup())

    async def _command_choose_task_handler(self, message: Message):
        """
        Process the incoming message with the task_id
        :param message:
        :return:
        """
        task_id = message.text
        first_name = message.from_user.first_name
        await message.answer(f'Отлично! Задача {task_id} была зарегистрирована за пользователем {first_name}',
                       reply_markup=ReplyKeyboardRemove())

    async def start_polling(self):
        self.dispatcher.message.register(self._command_start_handler, CommandStart())
        self.dispatcher.message.register(self._command_get_tasks_handler, Command('task_list'))
        self.dispatcher.message.register(self._command_choose_task_handler)
        await self.dispatcher.start_polling(self.bot)


async def main() -> None:
    bot = TaskBot(bot_token=BOT_TOKEN)
    await bot.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
