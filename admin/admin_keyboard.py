from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


admin_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Text', callback_data='text'),
            InlineKeyboardButton(text='Add_pic', callback_data='add_pic'),
            InlineKeyboardButton(text='Add_admin', callback_data='add_admin'),
            InlineKeyboardButton(text='Exit', callback_data='exit')
        ]
    ]
)
