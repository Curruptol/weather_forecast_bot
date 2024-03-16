import requests
import datetime
import config
from aiogram import Bot, types, Dispatcher, F
from aiogram.types import Message
from aiogram import F

bot = Bot(config.BOT_TOKEN)
dp = Dispatcher()


@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.last_name} {message.from_user.first_name}!\n"
                         f"Напиши название города")


async def send_weather(message: Message):
    pass

async def start_bot():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)