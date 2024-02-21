from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from keyboards.inlaine_button import select_menu_button, edit_button_word, delete_button
from cllasses.main_book import BibleTree
from make_pass import generate_password

dt = BibleTree()

router_callback_handler = Router()


@router_callback_handler.callback_query(F.data == 'menu')
async def call_menu(callback: CallbackQuery):
    await callback.message.edit_text(text='Виберіть кнопку', reply_markup=select_menu_button)
    await callback.answer('перехід в меню')


@router_callback_handler.callback_query(F.data == 'edit')
async def process_edit_message(callback: CallbackQuery):
    await callback.message.edit_text(text='next', reply_markup=edit_button_word)
    await callback.message.answer('word🔍')


@router_callback_handler.callback_query(F.data == 'yes')
async def proces_password(callback: CallbackQuery):
    await callback.message.answer('Ваш пароль')
    await callback.message.answer(generate_password(length=12), reply_markup=delete_button)
    await callback.answer('✅')


@router_callback_handler.callback_query(F.data == 'no')
async def proces_cancel(callback: CallbackQuery, bot: Bot):
    await bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    await callback.answer()
