import requests
import math
import asyncio
import config
import logging
from datetime import datetime as dt
from aiogram import Bot, types, Dispatcher, F
from aiogram.types import Message


bot = Bot(config.BOT_TOKEN)
dp = Dispatcher()

async def start_bot():
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

@dp.message(F.text == "/start")
async def start(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!")
    await message.answer(f"Напиши название города")

@dp.message()
async def send_weather(message: Message):
    try:
        req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?"
                           f"q={message.text}"
                           f"&lang=ru"
                           f"&units=metric"
                           f"&appid={config.OPEN_WEATHER_API_KEY}"
                           )
        request_data = req.json()
        # pprint(request_data)

        cur_city = request_data["name"]
        cur_temp = math.ceil(request_data["main"]["temp"])
        cur_humidity = request_data["main"]["humidity"]
        cur_pressure = request_data["main"]["pressure"]
        cur_feels_like = math.ceil(request_data["main"]["feels_like"])
        cur_temp_max = math.ceil(request_data["main"]["temp_max"])
        cur_temp_min = math.ceil(request_data["main"]["temp_min"])
        cur_timestamp_sunrise = dt.fromtimestamp(request_data["sys"]["sunrise"])
        cur_timestamp_sunset = dt.fromtimestamp(request_data["sys"]["sunset"])
        cur_sunrise = dt.time(cur_timestamp_sunrise)
        cur_sunset = dt.time(cur_timestamp_sunset)
        cur_day_len = cur_timestamp_sunset - cur_timestamp_sunrise

        await message.answer(f"Погода в городе {cur_city}\n"
                             f"Текущая температура: {cur_temp}, ощущается как {cur_feels_like}\n"
                             f"Макс. температура: {cur_temp_max}. Мин. температура: {cur_temp_min}\n"
                             f"Текущая влажность: {cur_humidity}\n"
                             f"Текущее давление {cur_pressure}\n"
                             f"Восход в {cur_sunrise}\n"
                             f"Закат в {cur_sunset}\n"
                             f"Продолжительность дня: {cur_day_len}"
                            )

    except Exception as exc:
        print(exc)
        print("Неверное название города")

# def get_weather(city, open_weather_api_key: config.OPEN_WEATHER_API_KEY):
#     try:
#         req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?"
#                            f"q={city}"
#                            f"&lang=ru"
#                            f"&units=metric"
#                            f"&appid={open_weather_api_key}"
#                            )
#         request_data = req.json()
#         # pprint(request_data)
#
#         cur_city = request_data["name"]
#         cur_temp = math.ceil(request_data["main"]["temp"])
#         cur_humidity = request_data["main"]["humidity"]
#         cur_pressure = request_data["main"]["pressure"]
#         cur_feels_like = math.ceil(request_data["main"]["feels_like"])
#         cur_temp_max = math.ceil(request_data["main"]["temp_max"])
#         cur_temp_min = math.ceil(request_data["main"]["temp_min"])
#         cur_timestamp_sunrise = dt.fromtimestamp(request_data["sys"]["sunrise"])
#         cur_timestamp_sunset = dt.fromtimestamp(request_data["sys"]["sunset"])
#         cur_sunrise = dt.time(cur_timestamp_sunrise)
#         cur_sunset = dt.time(cur_timestamp_sunset)
#         cur_day_len = cur_timestamp_sunset - cur_timestamp_sunrise
#
#         print(f"Погода в городе {cur_city}\n"
#               f"Текущая температура: {cur_temp}, ощущается как {cur_feels_like}\n"
#               f"Макс. температура: {cur_temp_max}. Мин. температура: {cur_temp_min}\n"
#               f"Текущая влажность: {cur_humidity}\n"
#               f"Текущее давление {cur_pressure}\n"
#               f"Восход в {cur_sunrise}\n"
#               f"Закат в {cur_sunset}\n"
#               f"Продолжительность дня: {cur_day_len}"
#              )
#
#     except Exception as exc:
#         print(exc)
#         print("Неверное название города")

def main():
    pass
    # city = input("Введите город:\n")
    # get_weather(city, config.OPEN_WEATHER_API_KEY)

if __name__ == '__main__':
    asyncio.run(start_bot())
    # main()
