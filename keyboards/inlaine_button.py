from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
            InlineKeyboardButton(text='Stickers🎁', url='https://t.me/addstickers/Hollytext')
        ],
        [
            InlineKeyboardButton(text='Про UaBible', callback_data='pro'),
            InlineKeyboardButton(text='add', url='https://t.me/ukr_bible_bot?startgroup=true')
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
