from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from domains.main.application.port.input.family_manager import FamilyManagerInterface

create_family_router = Router()


class CreateFamilyStates(StatesGroup):
    set_family_name = State()


@create_family_router.message(Command('new_family'))
async def _command_new_family_handler(message: Message, state: FSMContext):
    """
    Process the /new_family command
    """
    await state.set_state(CreateFamilyStates.set_family_name)
    await message.answer(f'Введите название семьи:')


@create_family_router.message(CreateFamilyStates.set_family_name)
async def create_family(message: Message, state: FSMContext, family_manager: FamilyManagerInterface):
    print('creating new family...')
    family_name = message.text
    await state.set_state(CreateFamilyStates.set_family_name)
    await family_manager.create_family(family_name=family_name, user_id=message.from_user.id)
    await message.answer(f'Семья {family_name} успешно создана!')
