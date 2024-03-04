from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery

from cllasses.main_book import BibleTree
from cllasses.call_filters import CallFilter
from keyboards.inlaine_button import start_menu
from aiogram.enums import ChatAction


index_books = BibleTree()
constructor_index = Router()


@constructor_index.callback_query(F.data == 'books')
async def create_book_kb(callback: CallbackQuery, bot: Bot):
    try:
        await bot.send_chat_action(callback.message.chat.id, ChatAction.TYPING)
        builder = InlineKeyboardBuilder()
        for i, j in index_books.get_name().items():
            builder.button(
                text=i,
                callback_data=CallFilter(foo='my', bar=j)
            )
        builder.adjust(3)
        builder.as_markup()
        await callback.message.edit_text(text='Виберіть книгу', reply_markup=builder.as_markup())
        await callback.answer('📖')
    except KeyError as e:
        await callback.message.reply(text=f'Технічна помилка {e} повторіть пізніше :( /help')


@constructor_index.callback_query(CallFilter.filter(F.foo == 'my'))
async def create_index_kb(callback: CallbackQuery, bot: Bot, callback_data: CallFilter):
    try:
        await bot.send_chat_action(callback.message.chat.id, ChatAction.TYPING)
        book_id = callback_data.bar.split("_")[0]
        builder = InlineKeyboardBuilder()
        for i, j in index_books.get_book(book_id=book_id).items():
            builder.button(
                text=i,
                callback_data=CallFilter(foo='section', bar=j)
            )
        builder.adjust(3)
        builder.as_markup()
        await callback.message.edit_text(text='Виберіть розділ', reply_markup=builder.as_markup())
        await callback.answer('📖')
    except KeyError as e:
        await callback.message.reply(text=f'Технічна помилка {e} повторіть пізніше :( /help')


@constructor_index.callback_query(CallFilter.filter(F.foo == 'section'))
async def create_sections_kb(callback: CallbackQuery, bot: Bot, callback_data: CallFilter):
    try:
        await bot.send_chat_action(callback.message.chat.id, ChatAction.TYPING)
        chapters_id = callback_data.bar.split(':')[0]
        builder = InlineKeyboardBuilder()
        for i, j in index_books.get_chapters(chapters_id=chapters_id).items():
            builder.button(
                text=i,
                callback_data=CallFilter(foo='verses', bar=j)
            )
        builder.adjust(3)
        await callback.message.edit_text(text='Виберіть вірш', reply_markup=builder.as_markup())
        await callback.answer('📖')
    except KeyError as e:
        await callback.message.reply(text=f'Технічна помилка {e} повторіть пізніше :( /help')


@constructor_index.callback_query(CallFilter.filter(F.foo == 'verses'))
async def get_verses(callback: CallbackQuery, bot: Bot, callback_data: CallFilter):
    try:
        await bot.send_chat_action(callback.message.chat.id, ChatAction.TYPING)
        verses = callback_data.bar.split('_')[0]
        answer = index_books.get_text_verses(verses=verses)
        await callback.message.answer(text=answer, reply_markup=start_menu)
        await callback.answer('📖')
    except KeyError as e:
        await callback.message.reply(text=f'Технічна помилка {e} повторіть пізніше :( /help')

