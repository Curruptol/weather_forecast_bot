import requests
import math
import os
from datetime import datetime as dt
from current_weather import WeatherData


def get_current_weather(city: str) -> str | None:
    """
    используется get запрос api open weather, результирующий json десериализуется и
    из значений объектов составляется текст прогноза погоды

    :param city: наименование города по-русски или по-ангийски
    :return: текст с прозногом погоды на сегодня, если статус код 200 или None, если статус код != 200
    """
    api = (f"https://api.openweathermap.org/data/2.5/weather?"
           f"q={city}"
           f"&lang=ru"
           f"&units=metric"
           f"&appid={os.environ['OPEN_WEATHER_API_KEY']}")
    req = requests.get(api)  # get request

    if req.status_code == 200:
        request_data = req.json()  # сохраняем результат в json
        current_weather = WeatherData(**request_data)  # десереализуем json

        city = current_weather.get("name")
        temp = math.ceil(current_weather.main.get("temp"))
        humidity = current_weather.main.get("humidity")
        pressure = math.ceil((current_weather.main.get("pressure")) / 1.333)  # переводим в мм.рт.ст.
        feels_like = math.ceil(current_weather.main.get("feels_like"))
        temp_max = math.ceil(current_weather.main.get("temp_max"))
        temp_min = math.ceil(current_weather.main.get("temp_min"))
        timestamp_sunrise = dt.fromtimestamp(current_weather.sys.get("sunrise"))
        timestamp_sunset = dt.fromtimestamp(current_weather.sys.get("sunset"))
        sunrise = dt.time(timestamp_sunrise)  # из unix timestamp получаем HH:MM:SS
        sunset = dt.time(timestamp_sunset)  # из unix timestamp получаем HH:MM:SS
        day_len = timestamp_sunset - timestamp_sunrise  # вычисляем длительность солнечного дня HH:MM:SS
        wind_speed = current_weather.wind.get("speed")
        wind_gust = current_weather.wind.get("gust")
        weather = current_weather.weather[0].get("description")
        weather_capitalize = weather.capitalize()
        clouds = current_weather.clouds.get("all")

        total_weather = (f"☀️Текущая погода в городе {city}: {weather_capitalize}\n\n"
                         f"☁️Облачность: {clouds}%\n"
                         f"🌡️Температура: {temp} C°. Ощущается как {feels_like} C°\n"
                         f"📈Макс. температура: {temp_max} C°\n"
                         f"📉Мин. температура: {temp_min} C°\n"
                         f"💧Влажность: {humidity}%\n"
                         f"🌀Давление {pressure} мм.рт.ст.\n"
                         f"🌅Восход в {sunrise}\n"
                         f"🌄Закат в {sunset}\n"
                         f"⏰Продолжительность дня: {day_len}\n\n"
                         f"💨Скорость ветра {wind_speed} м/с"
                         f"{f', порывы до {wind_gust} м/с' if wind_gust is not None else ''}")
        return total_weather
    else:
        return None
