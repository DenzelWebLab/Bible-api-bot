from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router

from cllasses.main_book import BibleTree
from keyboards.inlaine_button import delete_button, choice_button


bt = BibleTree()
commands_router = Router()


@commands_router.message(Command('list_index'))
async def get_list_index(message: Message):
    for i, j in bt.get_name().items():
        key = i
        values = j
        await message.answer(text=f'Індекс книги {key}: {values}')


@commands_router.message(Command('help'))
async def get_help(message: Message):
    await message.answer(text='Якщо не спрацювала кнопка просто перезавантаж бота /start', reply_markup=delete_button)


@commands_router.message(Command('password'))
async def get_password(message: Message):
    await message.answer(text='Опція створити пароль:\n'
                              'Бот може створити надійний пароль\nСтворити пароль?', reply_markup=choice_button)
