import requests
import math
import os
from datetime import datetime as dt


def get_weather(city):
    req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?"
                       f"q={city}"
                       f"&lang=ru"
                       f"&units=metric"
                       f"&appid={os.environ['OPEN_WEATHER_API_KEY']}"
                       )
    if req.status_code == 200:
        request_data = req.json()
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
        cur_wind_gust = request_data["wind"].get("gust")
        cur_weather = request_data["weather"][0]["description"]
        cur_weather_capitalize = cur_weather.capitalize()
        cur_clouds = request_data["clouds"]["all"]
        weather_for_answer = (f"☀️Текущая погода в городе {cur_city}:\n\n"
                              f"{cur_weather_capitalize}. ☁️Облачность: {cur_clouds}%\n"
                              f"🌡️Температура: {cur_temp} C°\n"
                              f"Ощущается как {cur_feels_like} C°\n"
                              f"Макс. температура: {cur_temp_max} C°\n"
                              f"Мин. температура: {cur_temp_min} C°\n"
                              f"💧Влажность: {cur_humidity}%\n"
                              f"Давление {cur_pressure} мм.рт.ст.\n"
                              f"🌅Восход в {cur_sunrise}\n"
                              f"🌄Закат в {cur_sunset}\n"
                              f"⏰Продолжительность дня: {cur_day_len}\n\n"
                              f"💨Скорость ветра {cur_wind_speed} м/с"
                              f"{f', порывы до {cur_wind_gust} м / с' if cur_wind_gust is not None else ''}"
                              )
        return weather_for_answer
    else:
        weather_for_answer = "❗️Неверный город❗️"
        return weather_for_answer
