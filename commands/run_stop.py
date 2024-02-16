from aiogram import Bot

from config import ADMIN_ID


async def start_bot(bot: Bot):
    await bot.send_message(chat_id=ADMIN_ID, text='Бот запущено')


async def stop_bot(bot: Bot):
    await bot.send_message(chat_id=ADMIN_ID, text='Бот зупинено')
