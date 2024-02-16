from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram import Router, F, Bot

from states.save_state_bot import StateIndex
from config import ADMIN_ID
from cllasses.index_ import IndexSearch
from keyboards.inlaine_button import edit_button_index

index_s = IndexSearch()
index_start_router = Router()
index_next_router = Router()


@index_start_router.callback_query(F.data == 'index')
async def start_index(callback: CallbackQuery, state: FSMContext):
    await state.set_state(StateIndex.index)
    await callback.message.answer(text='🔻Вибрана опція пошуку по індексу\n'
                                       '❗️Для коректного вводу  використати великі англійські літери\n'
                                       '❗️Приклад вводу: MAT.1.1\n'
                                       '❗️Три літери це індекс книги\n'
                                       '❗️Перша цифра це номер глави\n'
                                       '❗️Друга цифра це номер вірша')

    await callback.answer('🔍')


@index_start_router.message(StateIndex.index)
async def next_index_step(message: Message, bot: Bot, state: FSMContext):
    index = message.text.strip()
    answer_text = index_s.get_index(index=index)
    try:
        await message.answer(text=answer_text, reply_markup=edit_button_index)
    except KeyError as e:
        await bot.send_message(ADMIN_ID, text=f'error: {e}')

    finally:
        await state.clear()


