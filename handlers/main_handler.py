from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F

from data_bases.bot_users import BibleData
from cllasses.query import SearchQuery
from keyboards.inlaine_button import start_menu
from keyboards.inlaine_button import delete_button
from config import CONTACT
from filters.chat_filters import ChatTypeFilter
from admin.admi_filter import MyFilters


db = BibleData()
sq = SearchQuery()
router_main_handler = Router()
router_main_handler.message.filter(ChatTypeFilter(['private']))


@router_main_handler.message(CommandStart())
async def command_start_handler(message: Message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_name = message.from_user.username
    db.insert_user(user_id, user_first_name, user_name)
    button = start_menu
    await message.answer(f"*{message.from_user.first_name}*!\n"
                         f"Дякую що вибрали UaBible🇺🇦\n"
                         f"Це доступ до текстів української *Біблії* в telegram\n", reply_markup=button)


@router_main_handler.callback_query(F.data == 'pro')
async def get_copyright(callback: CallbackQuery):
    answer_text = sq.get_right()
    await callback.message.answer(text=answer_text, reply_markup=delete_button)
    await callback.answer('✅')


@router_main_handler.callback_query(F.data == 'info')
async def get_info(callback: CallbackQuery):
    await callback.message.answer(text=f'*Є питання* [пиши]({CONTACT})', reply_markup=delete_button)
    await callback.answer('❓')


@router_main_handler.callback_query(F.data == 'delete')
async def proces_delete(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()

