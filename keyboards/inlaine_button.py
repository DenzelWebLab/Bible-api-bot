from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Меню📁', callback_data='menu')
        ]
    ]
)

select_menu_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Книги📖', callback_data='books'),
            InlineKeyboardButton(text='❓', callback_data='info')
        ],
        [
            InlineKeyboardButton(text='Пошук по слову🔍', callback_data='word'),
            InlineKeyboardButton(text='Пошук по індексу🔍', callback_data='index')
        ],
        [
            InlineKeyboardButton(text='Яка сьогодні погода⛅️', callback_data='weather'),
            InlineKeyboardButton(text='Stickers🎁', url='https://t.me/addstickers/Hollytext')
        ],
        [
            InlineKeyboardButton(text='Про UaBible', callback_data='pro')
        ]
    ]
)

edit_button_word = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Оновити🔄', callback_data='word'),
            InlineKeyboardButton(text='Меню📁', callback_data='menu')
        ]
    ]
)

edit_button_index = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Оновити🔄', callback_data='index'),
            InlineKeyboardButton(text='Меню📁', callback_data='menu')
        ]
    ]
)

delete_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Зрозуміло✅', callback_data='delete')
        ]
    ]
)

choice_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Так', callback_data='yes'),
            InlineKeyboardButton(text='Ні', callback_data='no')
        ]
    ]
)

weather_update = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Оновити🔄', callback_data='weather')
        ]
    ]
)

