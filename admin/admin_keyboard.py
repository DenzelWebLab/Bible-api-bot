from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


admin_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Відправить текст БОТ', callback_data='text'),
            InlineKeyboardButton(text='Текст + картинка БОТ', callback_data='add_pic'),
            InlineKeyboardButton(text='Exit', callback_data='exit'),
            InlineKeyboardButton(text='Група', callback_data='group'),
            InlineKeyboardButton(text='Канал', callback_data='chanel')
        ]
    ]
)
