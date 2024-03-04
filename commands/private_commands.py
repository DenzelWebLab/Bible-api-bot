from aiogram.filters import Command
from aiogram.types import Message
from aiogram import Router


from cllasses.main_book import BibleTree
from keyboards.inlaine_button import delete_button, choice_button, select_menu_button


bt = BibleTree()
commands_router = Router()


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


@commands_router.message(Command('menu'))
async def get_menu(message: Message):
    await message.answer(text='MENU:', reply_markup=select_menu_button)
