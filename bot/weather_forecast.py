from dataclasses import dataclass
import json


@dataclass
class Location:
    name: str
    region: str
    country: str
    lat: float
    lon: float
    tz_id: str
    localtime_epoch: int
    localtime: str

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)


@dataclass
class Condition:
    text: str
    icon: str
    code: int

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)


@dataclass
class Current:
    last_updated_epoch: int
    last_updated: str
    temp_c: float
    temp_f: float
    is_day: int
    condition: Condition
    wind_mph: float
    wind_kph: float
    wind_degree: int
    wind_dir: str
    pressure_mb: float
    pressure_in: float
    precip_mm: float
    precip_in: float
    humidity: int
    cloud: int
    feelslike_c: float
    feelslike_f: float
    vis_km: float
    vis_miles: float
    uv: float
    gust_mph: float
    gust_kph: float

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)


@dataclass
class DayCondition:
    text: str
    icon: str
    code: int

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)


@dataclass
class Day:
    maxtemp_c: float
    maxtemp_f: float
    mintemp_c: float
    mintemp_f: float
    avgtemp_c: float
    avgtemp_f: float
    maxwind_mph: float
    maxwind_kph: float
    totalprecip_mm: float
    totalprecip_in: float
    totalsnow_cm: float
    avgvis_km: float
    avgvis_miles: float
    avghumidity: int
    daily_will_it_rain: int
    daily_chance_of_rain: int
    daily_will_it_snow: int
    daily_chance_of_snow: int
    condition: DayCondition
    uv: float

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)


@dataclass
class Astro:
    sunrise: str
    sunset: str
    moonrise: str
    moonset: str
    moon_phase: str
    moon_illumination: int
    is_moon_up: int
    is_sun_up: int

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)


@dataclass
class HourCondition:
    text: str
    icon: str
    code: int

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)


@dataclass
class Hour:
    time_epoch: int
    time: str
    temp_c: float
    temp_f: float
    is_day: int
    condition: HourCondition
    wind_mph: float
    wind_kph: float
    wind_degree: float
    wind_dir: str
    pressure_mb: float
    pressure_in: float
    precip_mm: float
    precip_in: float
    snow_cm: float
    humidity: int
    cloud: int
    feelslike_c: float
    feelslike_f: float
    windchill_c: float
    windchill_f: float
    heatindex_c: float
    heatindex_f: float
    dewpoint_c: float
    dewpoint_f: float
    will_it_rain: int
    chance_of_rain: int
    will_it_snow: int
    chance_of_snow: int
    vis_km: float
    vis_miles: float
    gust_mph: float
    gust_kph: float
    uv: float
    short_rad: float
    diff_rad: float

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)


@dataclass
class Forecastday:
    date: str
    date_epoch: str
    day: Day
    astro: Astro
    hour: list[Hour]

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)


@dataclass
class Forecast:
    forecastday: list[Forecastday]

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)


@dataclass
class WeatherForecastData:
    location: Location
    current: Current
    forecast: Forecast

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)
