import logging

from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from domains.main.application.port.input.family_manager import FamilyManagerInterface
from domains.main.application.port.input.user_manager import UserManagerInterface

create_family_router = Router()
logger = logging.getLogger(__name__)


class CreateFamilyStates(StatesGroup):
    set_family_name = State()


@create_family_router.message(Command('new_family'))
async def _command_new_family_handler(message: Message, state: FSMContext, user_manager: UserManagerInterface):
    """
    Process the /new_family command
    """
    user = await user_manager.get_user(message.from_user.id)
    if user.family_id:
        await message.answer(f'Вы уже состоите в семье {user.family_id}')
        await state.clear()
    await state.set_state(CreateFamilyStates.set_family_name)
    await message.answer(f'Введите название семьи:')


@create_family_router.message(CreateFamilyStates.set_family_name)
async def create_family(message: Message, state: FSMContext, family_manager: FamilyManagerInterface):
    logger.info("Creating new family for user", extra={"user_id": message.from_user.id,
                                                       "user_name": message.from_user.username,
                                                       "family_name": message.text})
    family_name = message.text
    await state.set_state(CreateFamilyStates.set_family_name)
    await family_manager.create_family(family_name=family_name, tg_user_id=message.from_user.id)
    await message.answer(f'Семья {family_name} успешно создана!')
    await state.clear()
