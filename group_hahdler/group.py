from aiogram import Router, F, Bot
from aiogram.filters import Command
from aiogram.types import Message, ChatMemberUpdated
from aiogram.filters import ChatMemberUpdatedFilter, JOIN_TRANSITION
from aiogram.exceptions import TelegramForbiddenError

from api.bibleAPI import BibleApi
from filters.checktype_chat import ChatTypeFilter


group_router = Router()


group_router.message.filter(ChatTypeFilter(['group', 'supergroup']))


@group_router.message(Command("start"))
async def start_group(message: Message):
    await message.answer(text='Вітаю я BiblebotUa ось що я вмію 👉 /help')


@group_router.message(F.text.startswith('-s'))
async def get_index_data_(message: Message):
    try:
        index = message.text.upper().split()[1]
        ba = BibleApi(index=index)
        answer = ba.get_index_data()
        await message.answer(text=answer)
    except KeyError:
        await message.answer(text='Невірний формат')


@group_router.message(F.text.startswith('-w'))
async def get_world_data(message: Message):
    try:
        query = message.text.split()[1]
        ba = BibleApi(query=query)
        answer = ba.get_query_data()
        await message.answer(text=answer)
    except KeyError:
        await message.answer(text='Невірний формат')


@group_router.message(Command('search'))
async def get_rules(message: Message, bot: Bot):
    try:
        await bot.send_message(chat_id=message.from_user.id,
                               text=f"{message.from_user.full_name}\n"
                                    "*Для отримання тексту наступні ключі*\n"
                                    "Тільки для групового чату\n"
                                    "-s пошук за індексом англ літери MAT.1.1\n"
                                    "-w пошук по слову або декілька укр літери"
                               )
    except TelegramForbiddenError:
        await message.reply(text='Будь ласка, почніть із команди /start.')


# вітаємо users
@group_router.chat_member(ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))
async def wellcome_user(event: ChatMemberUpdated, bot: Bot):
    news_user = event.new_chat_member.user
    await bot.send_message(chat_id=event.chat.id, text=f'Вітаємо тебе {news_user.full_name}\n'
                                                       f'в нашій групі🎉\n'
                                                       f'Правила /help')
