from aiogram import Bot, Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from data_bases.bot_users import BibleData

from admin.admin_keyboard import admin_button
from config import ADMIN_ID
from admin.state_admin import StateAdmins

admin_router = Router()
db = BibleData()


@admin_router.message(Command('admin'))
async def create_admin_kb(message: Message):
    if message.from_user.id == ADMIN_ID:
        await message.answer('Hi admin! select options:', reply_markup=admin_button)
    else:
        await message.reply('Ви не адміністратор бота🔒')


@admin_router.callback_query(F.data == 'exit')
async def hide_kb(call: CallbackQuery, bot: Bot):
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await call.answer('bay, admin')


@admin_router.callback_query(F.data == 'text')
async def start_proces_text(call: CallbackQuery, state: FSMContext):
    await state.set_state(StateAdmins.text)
    await call.message.answer(text='Enter text for message')
    await call.answer('text')


@admin_router.message(StateAdmins.text)
async def next_step_text(message: Message, bot: Bot, state: FSMContext):
    text = message.text.strip()
    db.cursor.execute("SELECT user_id FROM user_bible")
    users = db.cursor.fetchall()
    for user_id in users:
        try:
            await bot.send_message(user_id[0], text=text)
        except Exception as e:
            await message.answer(f'error: {e}')
    await state.clear()
