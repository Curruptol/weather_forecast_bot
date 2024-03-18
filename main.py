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
    req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?"
                       f"q={message.text}"
                       f"&lang=ru"
                       f"&units=metric"
                       f"&appid={config.OPEN_WEATHER_API_KEY}"
                       )
    if req.status_code == 200:
        request_data = req.json()
        # pprint(request_data)

        cur_city = request_data["name"]
        cur_temp = math.ceil(request_data["main"]["temp"])
        cur_humidity = request_data["main"]["humidity"]
        cur_pressure = math.ceil((request_data["main"]["pressure"]) / 1.333)
        cur_feels_like = math.ceil(request_data["main"]["feels_like"])
        cur_temp_max = math.ceil(request_data["main"]["temp_max"])
        cur_temp_min = math.ceil(request_data["main"]["temp_min"])
        cur_timestamp_sunrise = dt.fromtimestamp(request_data["sys"]["sunrise"])
        cur_timestamp_sunset = dt.fromtimestamp(request_data["sys"]["sunset"])
        cur_sunrise = dt.time(cur_timestamp_sunrise)
        cur_sunset = dt.time(cur_timestamp_sunset)
        cur_day_len = cur_timestamp_sunset - cur_timestamp_sunrise
        cur_wind_speed = request_data["wind"]["speed"]
        cur_wind_gust = request_data["wind"]["gust"]
        cur_weather = request_data["weather"][0]["description"]
        cur_weather_capitalize = cur_weather.capitalize()
        cur_clouds = request_data["clouds"]["all"]

        await message.answer(f"Текущая погода в городе {cur_city}\n"
                             f"{cur_weather_capitalize}. Облачность: {cur_clouds}%\n"
                             f"Температура: {cur_temp} C°, ощущается как {cur_feels_like} C°\n"
                             f"Макс. температура: {cur_temp_max} C°. Мин. температура: {cur_temp_min} C°\n"
                             f"Влажность: {cur_humidity}%\n"
                             f"Давление {cur_pressure} мм.рт.ст.\n"
                             f"Восход в {cur_sunrise}\n"
                             f"Закат в {cur_sunset}\n"
                             f"Продолжительность дня: {cur_day_len}\n\n"
                             f"Скорость ветра {cur_wind_speed} м/с, порывы до {cur_wind_gust} м/с"
                            )
    else:
        await message.answer(f"Неверный город")

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
