import requests
import math
import os
from datetime import datetime as dt
from weather_forecast import WeatherForecastData


def get_weather_forecast(city):
    api = (f"https://api.weatherapi.com/v1/forecast.json?"
           f"q={city}"
           f"&days=2"
           f"&aqi=no"
           f"&lang=ru"
           f"&hour=14"
           f"&alerts=no"
           f"&tides=no"
           f"&key={os.environ['WEATHERAPI_API_KEY']}")
    req = requests.get(api)

    if req.status_code == 200:
        request_data = req.json()
        weather_forecast = WeatherForecastData(**request_data)

        city = weather_forecast.get("location").get("name")

        date = weather_forecast.get("forecast").get("forecastday")[1].get("date")
        date = dt.strptime(date, "%Y-%m-%d").strftime('%d.%m.%Y')

        max_temp = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("maxtemp_c")
        max_temp = math.ceil(max_temp)

        min_temp = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("mintemp_c")
        min_temp = math.ceil(min_temp)

        avg_temp = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("avgtemp_c")
        avg_temp = math.ceil(avg_temp)

        max_wind_speed = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("maxwind_kph")
        max_wind_speed = max_wind_speed / 3.6
        max_wind_speed = round(max_wind_speed, 1)

        precipitation = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("totalprecip_mm")

        avg_humidity = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("avghumidity")

        chance_of_rain = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("daily_chance_of_rain")

        weather_condition = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("condition").get("text")

        sunrise = weather_forecast.get("forecast").get("forecastday")[1].get("astro").get("sunrise")
        sunrise = dt.strptime(sunrise, "%I:%M %p")
        sunrise = dt.strftime(sunrise, "%H:%M")

        sunset = weather_forecast.get("forecast").get("forecastday")[1].get("astro").get("sunset")
        sunset = dt.strptime(sunset, "%I:%M %p")
        sunset = dt.strftime(sunset, "%H:%M")

        pressure = weather_forecast.get("forecast").get("forecastday")[1].get("hour")[0].get("pressure_mb")
        pressure = pressure / 1.333
        pressure = round(pressure)

        cloud = weather_forecast.get("forecast").get("forecastday")[1].get("hour")[0].get("cloud")

        gust = weather_forecast.get("forecast").get("forecastday")[1].get("hour")[0].get("gust_kph")
        gust = gust / 3.6
        gust = round(gust, 1)

        total_weather_forecast = (f"☀️Погода на завтра {date} в городе {city}: {weather_condition}\n\n"
                                  f"📈Макс температура: {max_temp}C°\n"
                                  f"📉Мин температура: {min_temp}C°\n"
                                  f"🌡️Температура: {avg_temp}C°\n"
                                  f"☁️Облачность: {cloud}%\n"
                                  f"🌧️Вероятность дождя: {chance_of_rain}%\n"
                                  f"☔️Осадки {precipitation} мм\n"
                                  f"💧Влажность: {avg_humidity}%\n"
                                  f"🌀Давление: {pressure} мм.рт.ст.\n"
                                  f"🌅Восход в {sunrise}\n"
                                  f"🌄Закат в {sunset}\n"
                                  f"💨Скорость ветра до {max_wind_speed} м/с\n"
                                  f"💨Порывы ветра до {gust} м/с")
        return total_weather_forecast
    else:
        return None
