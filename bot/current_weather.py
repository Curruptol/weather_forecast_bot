from dataclasses import dataclass
from typing import Optional


@dataclass
class Coord:
    lon: float
    lat: float

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)


@dataclass
class Weather:
    id: int
    main: str
    description: str
    icon: str

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)


@dataclass
class Main:
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: Optional[int] = None
    grnd_level: Optional[int] = None

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)


@dataclass
class Wind:
    speed: float
    deg: int
    gust: Optional[int] = None

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)


@dataclass
class Rain:
    one_hour: float = None
    three_hours: float = None

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)


@dataclass
class Snow:
    one_hour: float = None
    three_hours: float = None

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)


@dataclass
class Clouds:
    all: int

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)


@dataclass
class Sys:
    type: int
    id: int
    country: str
    sunrise: int
    sunset: int
    message: str = None

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)


@dataclass
class WeatherData:
    coord: Coord
    weather: list[Weather]
    base: str
    main: Main
    wind: Wind
    clouds: Clouds
    dt: int
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: int
    rain: Optional[Rain] = None
    snow: Optional[Snow] = None
    visibility: Optional[int] = None

    def __getattr__(self, key):
        return super().__getattribute__(key)

    def get(self, key):
        return self.__getattr__(key)
