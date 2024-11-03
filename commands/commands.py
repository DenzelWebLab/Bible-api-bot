from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router
from aiogram.utils.markdown import hbold, hblockquote

from keyboards.inlaine_button import delete_button


commands_router = Router()


@commands_router.message(Command('help'))
async def get_help(message: Message):
    await message.answer(text=f"{hbold('Для користування в приватному чаті')}\n"
                              f"{hblockquote('Доступ до тексту через клавіатуру')}\n"
                              f"{hbold('Для груп')}\n"
                              f"{hblockquote('-s пошук за індексом англ літери MAT.1.1', sep='n')}")
