from aiogram.types import Message
from aiogram import F, Router

from config import CONTACT
from filters.chat_filters import ChatTypeFilter
from keyboards.inlaine_button import delete_button

filter_router = Router()
filter_router.message.filter(ChatTypeFilter(['private']))


@filter_router.message(F.text)
async def process_unknown_write_bots(message: Message):
    await message.delete()
    await message.answer(text=f'Для взаємодії з ботом використовуй кнопки\n'
                              f'або [пиши]({CONTACT}) в чат', reply_markup=delete_button)
    

