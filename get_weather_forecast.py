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

        city = weather_forecast.location.get("name") # город
        date = weather_forecast.forecast.forecastday[1].get("date") # завтрашняя дата YYYY-MM-DD
        max_temp = math.ceil(weather_forecast.forecast.forecastday[1].day.get("maxtemp_c")) # макс температура с точкой
        min_temp = math.ceil(weather_forecast.forecast.forecastday[1].day.get("mintemp_c")) # мин температура с точкой
        avg_temp = math.ceil(weather_forecast.forecast.forecastday[1].day.get("avgtemp_c")) # средняя температура с точкой
        max_wind_speed = (weather_forecast.forecast.forecastday[1].day.get("maxwind_kph")) / 3.6 # макс скорость ветра м/с
        precipitation = weather_forecast.forecast.forecastday[1].day.get("totalprecip_mm") # осадки мм
        avg_humidity = weather_forecast.forecast.forecastday[1].day.get("avghumidity") # ср влажность %
        chance_of_rain = weather_forecast.forecast.forecastday[1].day.get("daily_chance_of_rain") # вероятность дождя %
        weather_condition = weather_forecast.forecast.forecastday[1].day.condition.get("text") # погодные условия
        sunrise = weather_forecast.forecast.forecastday[1].astro.get("sunrise") # восход солнца XX:YY AM/PM
        sunset = weather_forecast.forecast.forecastday[1].astro.get("sunset") # закат солнца XX:YY AM/PM
        pressure = (weather_forecast.forecast.forecastday[1].hour[0].get("pressure_mb")) / 1.333 # среднее давление миллибары
        cloud = weather_forecast.forecast.forecastday[1].hour[0].get("cloud") # средняя облачность %
        gust = (weather_forecast.forecast.forecastday[1].hour[0].get("gust_kph")) / 3.6 # порывы ветра км/ч





