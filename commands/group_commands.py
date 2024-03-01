from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

from keyboards.inlaine_button import delete_button
from filters.chat_filters import ChatTypeFilter


grope_router = Router()
grope_router.message.filter(ChatTypeFilter(['group', 'supergroup']))


@grope_router.message(Command('rules'))
async def get_rules(message: Message):
    await message.answer(text='Правила чата:\n'
                              '1.Не ображати учасників\n'
                              '2.Спілкуватись можна на любу тему, але краще обговорювати духовні теми\n'
                              '3.Реклама заборонена\n'
                              '4.Продавати, міняти також заборонено\n'
                              'За порушення правил ban та видалення із чату', reply_markup=delete_button)
