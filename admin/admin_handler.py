from aiogram import Bot, Router, F, exceptions
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


from data_bases.bot_users import BibleData
from admin.admin_keyboard import admin_button
from admin.state_admin import StateAdmins
from filters.chat_filters import IsAdmin

admin_router = Router()
admin_router.message.filter(IsAdmin())
db = BibleData()


@admin_router.message(Command('admin'))
async def create_admin_kb(message: Message):
    await message.answer('Hi admin! select options:', reply_markup=admin_button)
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


@admin_router.callback_query(F.data == 'add_pic')
async def start_proces_add_pic(call: CallbackQuery, state: FSMContext):
    await state.set_state(StateAdmins.text_pic)
    await call.message.answer(text='Enter text for pic')
    await call.answer('text')


@admin_router.message(StateAdmins.text_pic)
async def next_step(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await state.set_state(StateAdmins.pic)
    await message.answer(text='Add pic')


@admin_router.message(StateAdmins.pic, F.photo)
async def add_pic(message: Message, bot: Bot, state: FSMContext):
    photo = message.photo[-1].file_id
    data = await state.get_data()
    text = data['text']

    db.cursor.execute("SELECT user_id FROM user_bible")
    users = db.cursor.fetchall()
    for user_id in users:
        try:
            await bot.send_photo(user_id[0], photo, caption=text)
        except exceptions.TelegramAPIError as e:
            print(f'Error type: {e}')
    await state.clear()
    await message.answer('Message send :)')
