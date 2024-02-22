from aiogram.types import Message
from aiogram import F, Router
from filters.chat_filters import ChatTypeFilter

filter_router = Router()
filter_router.message.filter(ChatTypeFilter(['private']))


@filter_router.message(F.text)
async def process_unknown_write_bots(message: Message):
    await message.reply(text='Я тебе не розумію :( /help')

