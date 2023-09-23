import logging

from aiogram import Bot, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.webhook import SendMessage
from aiogram.utils.executor import start_webhook
from environs import Env

env = Env()
env.read_env()
TOKEN = env.str('BOT_TOKEN')

WEBHOOK_HOST = 'https://71c7-176-52-113-151.ngrok-free.app'
WEBHOOK_PATH = ''
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '127.0.0.1'
WEBAPP_PORT = '8000'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

async def on_shutdown(dp):
    await bot.delete_webhook()

@dp.message_handler(commands=['start'])
async def start(mess:types.Message):
    return SendMessage(mess.chat_id, 'Вы написали боту /start')

@dp.message_handler(commands=['help'])
async def start(mess:types.Message):
    return SendMessage(mess.chat_id, 'Вы написали боту /help')

@dp.message_handler()
async def handler(mess: types.Message):
    return SendMessage(mess.chat_id, f'{mess}')


if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT
    )