from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from aiogram.types import CallbackQuery, Message


from states.save_state_bot import StateWord
from cllasses.query import SearchQuery
from keyboards.inlaine_button import edit_button_word


process_state_word = Router()
next_step_for_word = Router()
sq = SearchQuery()


@process_state_word.callback_query(F.data == 'word')
async def start_process_index(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(text='🔻Вибрана опція пошуку по ключовому слову\n'
                                       'Мова воду *українська*\n'
                                       'Для відміни /cancel')
    await state.set_state(StateWord.query_word)
    await callback.answer('word🔍')


@process_state_word.message(Command("cancel"))
@process_state_word.message(F.text.casefold() == "cancel")
async def cancel_handler(message: Message, state: FSMContext) -> None:
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.clear()
    await message.answer(text='Відмінено', reply_markup=edit_button_word)


@process_state_word.message(StateWord.query_word)
async def next_step(message: Message, state: FSMContext):
    word = message.text.strip().lower()
    try:
        if word:
            await state.update_data(word=word)
            text = sq.get_data(query=word)
            await message.answer(text, reply_markup=edit_button_word)
            await state.clear()
        else:
            await message.reply(text='Невірний формат', reply_markup=edit_button_word)
    except Exception as e:
        await message.reply(f'Невірний формат {e}', reply_markup=edit_button_word)


@process_state_word.message(StateWord.query_word)
async def process_unknown_write_bots(message: Message):
    await message.reply(text='Я тебе не розумію :(', reply_markup=edit_button_word)


