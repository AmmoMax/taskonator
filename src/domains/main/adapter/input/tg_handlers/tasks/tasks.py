from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from domains.main.application.port.input.task_manager import TaskManagerInterface

tasks_router = Router()


@tasks_router.message(Command('task_list'))
async def get_available_tasks(message: Message, task_manager: TaskManagerInterface) -> None:
    """ Return the list of available tasks for the user within the family.
    Process the /task_list command.
    Should return the list of tasks with inline keyboard.
    """
    user_id = str(message.from_user.id)
    list_of_tasks = await task_manager.get_available_tasks(user_id=user_id)
    formatted_tasks_list = format_list_of_task(list_of_tasks)
    keyboard = _build_task_keyboard(list_of_tasks.keys())
    await message.answer("\n".join(formatted_tasks_list), reply_markup=keyboard.as_markup())


@tasks_router.message(Command('choose_task'))
async def choose_task(message: Message, user_manager, task_manager):
    """
    Process the incoming message with the task_id
    """
    task_id = message.text
    first_name = message.from_user.first_name
    user_id = message.from_user.id
    task_info = await task_manager.get_task_by_id(task_id=task_id)
    task_description = task_info.get('description')
    # TODO: вынести текст сообщения в конфиг
    await message.answer(f'Отлично! Задача {task_description} была зарегистрирована за пользователем {first_name}',
                         reply_markup=ReplyKeyboardRemove())
    # TODO: продумать логику по проверке назначения задания, напирмер если у пользователя уже есть задача
    assigned = await user_manager.assign_task(user_id=user_id, task_id=task_id)


def _build_task_keyboard(self, task_ids: list) -> ReplyKeyboardBuilder:
    builder = ReplyKeyboardBuilder()
    for task_id in task_ids:
        builder.button(text=task_id)
    return builder

def format_list_of_task(list_of_tasks: dict) -> list:
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