from aiogram.fsm.context import FSMContext
from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message

from states.save_state_bot import StateWord
from cllasses.query import SearchQuery

from keyboards.inlaine_button import edit_button
from config import admin_id

process_state_word = Router()
next_step_for_word = Router()
sq = SearchQuery()


@process_state_word.callback_query(F.data == 'word')
async def start_process_index(callback: CallbackQuery, bot: Bot, state: FSMContext):
    try:
        await callback.message.answer(text='🔻Вибрана опція пошуку по ключовому слову\n'
                                           'Мова воду *українська*')
        await state.set_state(StateWord.query_word)
        await callback.answer('word🔍')
    except Exception as e:
        await bot.send_message(chat_id=admin_id, text=f'error: {e}')
        await callback.message.reply(text='⚠️Ой, халепа щось зламалось вже працюємо над виправленням⏳')


@next_step_for_word.message(StateWord.query_word)
async def next_step(message: Message, bot: Bot, state: FSMContext):
    word = message.text.strip()
    if not str:
        await message.reply('enter str')
    text = sq.get_data(query=word)
    button = edit_button
    try:
        await message.answer(text, reply_markup=button)
        await state.clear()
    except Exception as e:
        await bot.send_message(chat_id=admin_id, text=f'error: {e}')
        await message.reply(text='Ой, халепа не вірний формат')
    except KeyError:
        await bot.send_message(chat_id=admin_id, text=f'error: {KeyError}')##???/
