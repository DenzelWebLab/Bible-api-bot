from aiogram.types import BotCommand


group = [
    BotCommand(command='start', description='Запуск бота'),
    BotCommand(command='help', description='Правила'),
    BotCommand(command='search', description='Пошук'),
    BotCommand(command='stop', description='Зупинити бота')
]

private = [
    BotCommand(command='start', description='Запуск бота'),
    BotCommand(command='help', description='Допомога')


]

admin = [
    BotCommand(command='start', description='start bot'),
    BotCommand(command='admin', description='admin menu')
    # BotCommand(command='', description=''),
    # BotCommand(command='', description=''),
    # BotCommand(command='', description='')
]
