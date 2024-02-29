from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram import Router, F
from aiogram.utils.keyboard import InlineKeyboardBuilder

from cllasses.main_book import BibleTree
from keyboards.inlaine_button import delete_button, choice_button
from filters.chat_filters import ChatTypeFilter



bt = BibleTree()
commands_router = Router()
commands_router.message.filter(ChatTypeFilter(['private']))


@commands_router.message(Command('list_index'))
async def get_list_index(message: Message):
    for i, j in bt.get_name().items():
        key = i
        values = j
        await message.answer(text=f'Індекс книги {key}: {values}')


@commands_router.message(Command('help'))
async def get_help(message: Message):
    await message.answer(text="Звідайтеся до наведеної нижче інструкції для використання бота з кнопками:\n"
                              "Натисніть  /start, щоб почати взаємодію з ботом або перезапустити."
                              "Оберіть потрібну вам опцію з переліку, натиснувши на відповідну кнопку."
                              "Якщо потрібно ввести текстову інформацію, вам буде надано"
                              " відповідне поле для введення тексту."
                              "Щоб повернутися назад або вийти з певного розділу, скористайтеся відповідною командою."
                              "Якщо є можливість обрати із декількох варіантів, зверніть "
                              "увагу на всі доступні кнопки та виберіть той, який відповідає вашим потребам."
                              "В будь-який момент ви можете завершити взаємодію"
                              " з ботом, натиснувши  команду /stop."
                              "Слідкуйте за інструкціями та користуйтеся кнопками для зручної взаємодії з ботом. :)",
                              reply_markup=delete_button)


@commands_router.message(Command('password'))
async def get_password(message: Message):
    await message.answer(text='Опція створити пароль:\n'
                              'Бот згенерує надійний пароль із 14 різних символів\n'
                              'Цікавий факт: щоб підібрати пароль із 14 символів в якому є маленькі та великі'
                              'букви і цифри потрібно буде *5 млрд. років* :)\n'
                              'Створити пароль?', reply_markup=choice_button)

# !!!
@commands_router.message(Command('psalm'))
async def get_psa(message: Message):
    builder = InlineKeyboardBuilder()
    for i, j in bt.get_psalm().items():
        builder.button(
            text=i,
            callback_data=j
        )
        builder.adjust(3)
        builder.as_markup()
        await message.answer('psa', reply_markup=builder.as_markup())


@commands_router.callback_query(F.data == "PSA")
async def get_psa_next(call: CallbackQuery):
    builder = InlineKeyboardBuilder()
    for i, j in range(1, 20, bt.get_psalm()):
        builder.button(
            text=i,
            callback_data=j
        )
        builder.adjust(3)
        await call.message.answer('psalm', reply_markup=builder.as_markup())
        await call.answer()
