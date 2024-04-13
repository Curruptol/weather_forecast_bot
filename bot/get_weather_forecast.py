import requests
import math
import os
from datetime import datetime as dt
from weather_forecast import WeatherForecastData


def get_weather_forecast(city: str, days: int) -> str | None:
    """

    :param city:
    :param days:
    :return:
    """
    api = (f"https://api.weatherapi.com/v1/forecast.json?"
           f"q={city}"
           f"&days=3"
           f"&aqi=no"
           f"&lang=ru"
           f"&hour=14"
           f"&alerts=no"
           f"&tides=no"
           f"&key={os.environ['WEATHERAPI_API_KEY']}")
    req = requests.get(api)

    if req.status_code == 200:
        if days == 2:
            request_data = req.json()
            weather_forecast = WeatherForecastData(**request_data)

            city = weather_forecast.get("location").get("name")

            date_1 = weather_forecast.get("forecast").get("forecastday")[1].get("date")
            date_1 = dt.strptime(date_1, "%Y-%m-%d").strftime('%d.%m.%Y')

            max_temp_1 = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("maxtemp_c")
            max_temp_1 = math.ceil(max_temp_1)

            min_temp_1 = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("mintemp_c")
            min_temp_1 = math.ceil(min_temp_1)

            avg_temp_1 = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("avgtemp_c")
            avg_temp_1 = math.ceil(avg_temp_1)

            max_wind_speed_1 = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("maxwind_kph")
            max_wind_speed_1 = max_wind_speed_1 / 3.6
            max_wind_speed_1 = round(max_wind_speed_1, 1)

            precipitation_1 = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("totalprecip_mm")

            avg_humidity_1 = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("avghumidity")

            chance_of_rain_1 = weather_forecast.get("forecast").get("forecastday")[1].get(
                "day").get("daily_chance_of_rain")

            weather_condition_1 = weather_forecast.get("forecast").get("forecastday")[1].get("day").get(
                "condition").get("text")

            sunrise_1 = weather_forecast.get("forecast").get("forecastday")[1].get("astro").get("sunrise")
            sunrise_1 = dt.strptime(sunrise_1, "%I:%M %p")
            sunrise_1 = dt.strftime(sunrise_1, "%H:%M")

            sunset_1 = weather_forecast.get("forecast").get("forecastday")[1].get("astro").get("sunset")
            sunset_1 = dt.strptime(sunset_1, "%I:%M %p")
            sunset_1 = dt.strftime(sunset_1, "%H:%M")

            pressure_1 = weather_forecast.get("forecast").get("forecastday")[1].get("hour")[0].get("pressure_mb")
            pressure_1 = pressure_1 / 1.333
            pressure_1 = round(pressure_1)

            cloud_1 = weather_forecast.get("forecast").get("forecastday")[1].get("hour")[0].get("cloud")

            gust_1 = weather_forecast.get("forecast").get("forecastday")[1].get("hour")[0].get("gust_kph")
            gust_1 = gust_1 / 3.6
            gust_1 = round(gust_1, 1)

            tomorrow_weather_forecast = (f"☀️Погода на завтра {date_1} в городе {city}: {weather_condition_1}\n\n"
                                     f"📈Макс температура: {max_temp_1}C°\n"
                                     f"📉Мин температура: {min_temp_1}C°\n"
                                     f"🌡️Температура: {avg_temp_1}C°\n"
                                     f"☁️Облачность: {cloud_1}%\n"
                                     f"🌧️Вероятность дождя: {chance_of_rain_1}%\n"
                                     f"☔️Осадки {precipitation_1} мм\n"
                                     f"💧Влажность: {avg_humidity_1}%\n"
                                     f"🌀Давление: {pressure_1} мм.рт.ст.\n"
                                     f"🌅Восход в {sunrise_1}\n"
                                     f"🌄Закат в {sunset_1}\n"
                                     f"💨Скорость ветра до {max_wind_speed_1} м/с\n"
                                     f"💨Порывы ветра до {gust_1} м/с")
            return tomorrow_weather_forecast
        elif days == 3:
            request_data = req.json()
            weather_forecast = WeatherForecastData(**request_data)

            city = weather_forecast.get("location").get("name")

            date_0 = weather_forecast.get("forecast").get("forecastday")[0].get("date")
            date_0 = dt.strptime(date_0, "%Y-%m-%d").strftime('%d.%m.%Y')
            date_1 = weather_forecast.get("forecast").get("forecastday")[1].get("date")
            date_1 = dt.strptime(date_1, "%Y-%m-%d").strftime('%d.%m.%Y')
            date_2 = weather_forecast.get("forecast").get("forecastday")[2].get("date")
            date_2 = dt.strptime(date_2, "%Y-%m-%d").strftime('%d.%m.%Y')

            max_temp_0 = weather_forecast.get("forecast").get("forecastday")[0].get("day").get("maxtemp_c")
            max_temp_0 = math.ceil(max_temp_0)
            max_temp_1 = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("maxtemp_c")
            max_temp_1 = math.ceil(max_temp_1)
            max_temp_2 = weather_forecast.get("forecast").get("forecastday")[2].get("day").get("maxtemp_c")
            max_temp_2 = math.ceil(max_temp_2)

            min_temp_0 = weather_forecast.get("forecast").get("forecastday")[0].get("day").get("mintemp_c")
            min_temp_0 = math.ceil(min_temp_0)
            min_temp_1 = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("mintemp_c")
            min_temp_1 = math.ceil(min_temp_1)
            min_temp_2 = weather_forecast.get("forecast").get("forecastday")[2].get("day").get("mintemp_c")
            min_temp_2 = math.ceil(min_temp_2)

            avg_temp_0 = weather_forecast.get("forecast").get("forecastday")[0].get("day").get("avgtemp_c")
            avg_temp_0 = math.ceil(avg_temp_0)
            avg_temp_1 = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("avgtemp_c")
            avg_temp_1 = math.ceil(avg_temp_1)
            avg_temp_2 = weather_forecast.get("forecast").get("forecastday")[2].get("day").get("avgtemp_c")
            avg_temp_2 = math.ceil(avg_temp_2)

            max_wind_speed_0 = weather_forecast.get("forecast").get("forecastday")[0].get("day").get("maxwind_kph")
            max_wind_speed_0 = max_wind_speed_0 / 3.6
            max_wind_speed_0 = round(max_wind_speed_0, 1)
            max_wind_speed_1 = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("maxwind_kph")
            max_wind_speed_1 = max_wind_speed_1 / 3.6
            max_wind_speed_1 = round(max_wind_speed_1, 1)
            max_wind_speed_2 = weather_forecast.get("forecast").get("forecastday")[2].get("day").get("maxwind_kph")
            max_wind_speed_2 = max_wind_speed_2 / 3.6
            max_wind_speed_2 = round(max_wind_speed_2, 1)

            precipitation_0 = weather_forecast.get("forecast").get("forecastday")[0].get("day").get("totalprecip_mm")
            precipitation_1 = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("totalprecip_mm")
            precipitation_2 = weather_forecast.get("forecast").get("forecastday")[2].get("day").get("totalprecip_mm")

            avg_humidity_0 = weather_forecast.get("forecast").get("forecastday")[0].get("day").get("avghumidity")
            avg_humidity_1 = weather_forecast.get("forecast").get("forecastday")[1].get("day").get("avghumidity")
            avg_humidity_2 = weather_forecast.get("forecast").get("forecastday")[2].get("day").get("avghumidity")

            chance_of_rain_0 = weather_forecast.get("forecast").get("forecastday")[0].get("day").get(
                "daily_chance_of_rain")
            chance_of_rain_1 = weather_forecast.get("forecast").get("forecastday")[1].get("day").get(
                "daily_chance_of_rain")
            chance_of_rain_2 = weather_forecast.get("forecast").get("forecastday")[2].get("day").get(
                "daily_chance_of_rain")

            weather_condition_0 = weather_forecast.get("forecast").get("forecastday")[0].get("day").get(
                "condition").get(
                "text")
            weather_condition_1 = weather_forecast.get("forecast").get("forecastday")[1].get("day").get(
                "condition").get(
                "text")
            weather_condition_2 = weather_forecast.get("forecast").get("forecastday")[2].get("day").get(
                "condition").get(
                "text")

            sunrise_0 = weather_forecast.get("forecast").get("forecastday")[0].get("astro").get("sunrise")
            sunrise_0 = dt.strptime(sunrise_0, "%I:%M %p")
            sunrise_0 = dt.strftime(sunrise_0, "%H:%M")
            sunrise_1 = weather_forecast.get("forecast").get("forecastday")[1].get("astro").get("sunrise")
            sunrise_1 = dt.strptime(sunrise_1, "%I:%M %p")
            sunrise_1 = dt.strftime(sunrise_1, "%H:%M")
            sunrise_2 = weather_forecast.get("forecast").get("forecastday")[2].get("astro").get("sunrise")
            sunrise_2 = dt.strptime(sunrise_2, "%I:%M %p")
            sunrise_2 = dt.strftime(sunrise_2, "%H:%M")

            sunset_0 = weather_forecast.get("forecast").get("forecastday")[0].get("astro").get("sunset")
            sunset_0 = dt.strptime(sunset_0, "%I:%M %p")
            sunset_0 = dt.strftime(sunset_0, "%H:%M")
            sunset_1 = weather_forecast.get("forecast").get("forecastday")[1].get("astro").get("sunset")
            sunset_1 = dt.strptime(sunset_1, "%I:%M %p")
            sunset_1 = dt.strftime(sunset_1, "%H:%M")
            sunset_2 = weather_forecast.get("forecast").get("forecastday")[2].get("astro").get("sunset")
            sunset_2 = dt.strptime(sunset_2, "%I:%M %p")
            sunset_2 = dt.strftime(sunset_2, "%H:%M")

            pressure_0 = weather_forecast.get("forecast").get("forecastday")[0].get("hour")[0].get("pressure_mb")
            pressure_0 = pressure_0 / 1.333
            pressure_0 = round(pressure_0)
            pressure_1 = weather_forecast.get("forecast").get("forecastday")[1].get("hour")[0].get("pressure_mb")
            pressure_1 = pressure_1 / 1.333
            pressure_1 = round(pressure_1)
            pressure_2 = weather_forecast.get("forecast").get("forecastday")[2].get("hour")[0].get("pressure_mb")
            pressure_2 = pressure_2 / 1.333
            pressure_2 = round(pressure_2)

            cloud_0 = weather_forecast.get("forecast").get("forecastday")[0].get("hour")[0].get("cloud")
            cloud_1 = weather_forecast.get("forecast").get("forecastday")[1].get("hour")[0].get("cloud")
            cloud_2 = weather_forecast.get("forecast").get("forecastday")[2].get("hour")[0].get("cloud")

            gust_0 = weather_forecast.get("forecast").get("forecastday")[0].get("hour")[0].get("gust_kph")
            gust_0 = gust_0 / 3.6
            gust_0 = round(gust_0, 1)
            gust_1 = weather_forecast.get("forecast").get("forecastday")[1].get("hour")[0].get("gust_kph")
            gust_1 = gust_1 / 3.6
            gust_1 = round(gust_1, 1)
            gust_2 = weather_forecast.get("forecast").get("forecastday")[2].get("hour")[0].get("gust_kph")
            gust_2 = gust_2 / 3.6
            gust_2 = round(gust_2, 1)

            first_day = (f"☀️Погода на сегодня {date_0}: {weather_condition_0}\n\n"
                         f"📈Макс температура: {max_temp_0}C°\n"
                         f"📉Мин температура: {min_temp_0}C°\n"
                         f"🌡️Температура: {avg_temp_0}C°\n"
                         f"☁️Облачность: {cloud_0}%\n"
                         f"🌧️Вероятность дождя: {chance_of_rain_0}%\n"
                         f"☔️Осадки {precipitation_0} мм\n"
                         f"💧Влажность: {avg_humidity_0}%\n"
                         f"🌀Давление: {pressure_0} мм.рт.ст.\n"
                         f"🌅Восход в {sunrise_0}\n"
                         f"🌄Закат в {sunset_0}\n"
                         f"💨Скорость ветра до {max_wind_speed_0} м/с\n"
                         f"💨Порывы ветра до {gust_0} м/с\n")

            second_day = (f"☀️Погода на завтра {date_1}: {weather_condition_1}\n\n"
                          f"📈Макс температура: {max_temp_1}C°\n"
                          f"📉Мин температура: {min_temp_1}C°\n"
                          f"🌡️Температура: {avg_temp_1}C°\n"
                          f"☁️Облачность: {cloud_1}%\n"
                          f"🌧️Вероятность дождя: {chance_of_rain_1}%\n"
                          f"☔️Осадки {precipitation_1} мм\n"
                          f"💧Влажность: {avg_humidity_1}%\n"
                          f"🌀Давление: {pressure_1} мм.рт.ст.\n"
                          f"🌅Восход в {sunrise_1}\n"
                          f"🌄Закат в {sunset_1}\n"
                          f"💨Скорость ветра до {max_wind_speed_1} м/с\n"
                          f"💨Порывы ветра до {gust_1} м/с\n")

            third_day = (f"☀️Погода на послезавтра {date_2}: {weather_condition_2}\n\n"
                         f"📈Макс температура: {max_temp_2}C°\n"
                         f"📉Мин температура: {min_temp_2}C°\n"
                         f"🌡️Температура: {avg_temp_2}C°\n"
                         f"☁️Облачность: {cloud_2}%\n"
                         f"🌧️Вероятность дождя: {chance_of_rain_2}%\n"
                         f"☔️Осадки {precipitation_2} мм\n"
                         f"💧Влажность: {avg_humidity_2}%\n"
                         f"🌀Давление: {pressure_2} мм.рт.ст.\n"
                         f"🌅Восход в {sunrise_2}\n"
                         f"🌄Закат в {sunset_2}\n"
                         f"💨Скорость ветра до {max_wind_speed_2} м/с\n"
                         f"💨Порывы ветра до {gust_2} м/с\n")

            three_days_weather_forecast = (f"📆Прогноз погоды в {city} на три дня:\n\n"
                                           f"{first_day}\n"
                                           f"{second_day}\n"
                                           f"{third_day}")
            return three_days_weather_forecast
    else:
        return None
