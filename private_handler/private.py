from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

from filters.call_filters import CallFilter
from filters.checktype_chat import ChatTypeFilter
from api.bibleAPI import BibleApi
from keyboards.bulderkb import builder_keyboard

private_router = Router()


private_router.message.filter(ChatTypeFilter(['private']))


@private_router.message(CommandStart)
async def start_bot(message: Message):
    await message.answer("Uabiblebot🇺🇦", reply_markup=builder_keyboard(
        ['📖', '🔎', '📜'],
        ['books', 'search', 'help'],
        sizes=2
    )
                             )


@private_router.callback_query(F.data == 'books')
async def create_book_kb(call: CallbackQuery):
    try:
        ba = BibleApi()
        builder = InlineKeyboardBuilder()
        for i, j in ba.get_book_name().items():
            builder.button(
                text=i,
                callback_data=CallFilter(foo='my', bar=j)
            )
        builder.adjust(3)
        builder.as_markup()
        await call.message.answer(text=f'{call.from_user.full_name}\nВибери книгу',
                                  reply_markup=builder.as_markup())
        await call.answer('📖')
    except KeyError:
        await call.message.answer(text=f'Технічна помилка  повторіть пізніше :( /help')


@private_router.callback_query(CallFilter.filter(F.foo == 'my'))
async def create_index_kb(callback: CallbackQuery, callback_data: CallFilter):
    try:
        book_id = callback_data.bar.split("_")[0]
        builder = InlineKeyboardBuilder()
        ba = BibleApi(book_id=book_id)
        for i, j in ba.get_book().items():
            builder.button(
                text=i,
                callback_data=CallFilter(foo='section', bar=j)
            )
        builder.adjust(3)
        builder.as_markup()
        await callback.message.edit_text(text='Виберіть розділ', reply_markup=builder.as_markup())
        await callback.answer('📖')
    except KeyError:
        await callback.message.reply(text=f'Технічна помилка повторіть пізніше :( /help')


@private_router.callback_query(CallFilter.filter(F.foo == 'section'))
async def create_sections_kb(callback: CallbackQuery, callback_data: CallFilter):
    try:
        chapters_id = callback_data.bar.split(':')[0]
        ba = BibleApi(chapter_id=chapters_id)
        builder = InlineKeyboardBuilder()
        for i, j in ba.get_chapter().items():
            builder.button(
                text=i,
                callback_data=CallFilter(foo='verses', bar=j)
            )
        builder.adjust(3)
        await callback.message.edit_text(text='Виберіть вірш', reply_markup=builder.as_markup())
        await callback.answer('📖')
    except KeyError:
        await callback.message.reply(text=f'Технічна помилка повторіть пізніше :( /help')


@private_router.callback_query(CallFilter.filter(F.foo == 'verses'))
async def get_verses(callback: CallbackQuery, callback_data: CallFilter):
    try:
        verses = callback_data.bar.split('_')[0]
        ba = BibleApi(verses=verses)
        answer = ba.get_verse()
        await callback.message.answer(text=answer, reply_markup=builder_keyboard(
            ['📖', '🔍'],
            ['books', 'search'],
            sizes=2
        ))
        await callback.answer('📖')
    except KeyError:
        await callback.message.reply(text=f'Технічна помилка повторіть пізніше :( /help')

