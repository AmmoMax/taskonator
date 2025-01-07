from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

start_router = Router()


@start_router.message(Command('start'))
async def start(message: Message):
    start_msg = ("Привет! Я бот для выполнения задач за бонусы.\n"
                 "Для просмотра доступных задач в вашей семье введите /task_list\n")
    await message.answer(start_msg)
