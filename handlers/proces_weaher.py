from aiogram.fsm.context import FSMContext
from aiogram import Router, F, Bot
from aiogram.types import CallbackQuery, Message

from states.save_state_bot import StateWeather
from cllasses.weather_info import Weather
from keyboards.inlaine_button import start_menu
from config import ADMIN_ID


weather_router = Router()
next_weather_step = Router()
wh = Weather()


@weather_router.callback_query(F.data == 'weather')
async def start_weather(callback: CallbackQuery, bot: Bot, state: FSMContext):
    await state.set_state(StateWeather.city)
    try:
        await callback.message.answer(text='🔻Опція погода\nВедіть назву міста:')

    except Exception as e:
        await bot.send_message(ADMIN_ID, f'error: {e}')
        await callback.message.answer('⚠️Невірний формат,ведіть назву міста!!!')
    finally:
        await callback.answer('🌤')


@next_weather_step.message(StateWeather.city)
async def next_step(message: Message, bot: Bot, state: FSMContext):
    name_city = message.text.strip()
    try:
        text_answer = wh.get_description(city=name_city)
        await message.answer(text_answer, reply_markup=start_menu)
    except Exception as e:
        await bot.send_message(ADMIN_ID, f'error: {e}', reply_markup=start_menu)
        await message.reply('⚠️Ой, халепа щось зламалось, вже працюєм над виправленням⏳')
    await state.clear()
