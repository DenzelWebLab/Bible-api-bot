from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram import Router, F, Bot

from states.save_state_bot import StateIndex
from config import admin_id
from cllasses.index_ import IndexSearch
from keyboards.inlaine_button import edit_button

index_s = IndexSearch()
index_start_router = Router()
index_next_router = Router()


@index_start_router.callback_query(F.data == 'index')
async def start_index(callback: CallbackQuery, bot: Bot, state: FSMContext):
    try:
        await state.set_state(StateIndex.index)
        await callback.message.answer(text='🔻Вибрана опція пошуку по індексу\n'
                                      '❗️Для коректного вводу  використати великі англійські літери\n'
                                      '❗️Приклад вводу: MAT.1.1\n'
                                      '❗️Три літери це індекс книги\n'
                                      '❗️Перша цифра це номер глави\n'
                                      '❗️Друга цифра це номер вірша')
        await callback.answer('🔍')
    except Exception as e:
        await bot.send_message(admin_id, text=f'error: {e}')


@index_next_router.message(StateIndex.index)
async def next_index_step(message: Message, bot: Bot, state: FSMContext):
    index = message.text.strip()
    if not str:
        await message.reply('Невірний формат')
    answer_text = index_s.get_index(index=index)
    try:
        await message.answer(text=answer_text, reply_markup=edit_button)
    except Exception as e:
        await bot.send_message(admin_id, text=f'error: {e}')

    finally:
        await state.clear()


