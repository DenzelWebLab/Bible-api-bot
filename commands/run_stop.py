from aiogram import Bot

from config import admin_id


async def start_bot(bot: Bot):
    await bot.send_message(chat_id=admin_id, text='Бот запущено')


async def stop_bot(bot: Bot):
    await bot.send_message(chat_id=admin_id, text='Бот зупинено')
