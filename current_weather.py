from dataclasses import dataclass
from typing import Optional


@dataclass
class Coord:
    lon: float
    lat: float


@dataclass
class Weather:
    id: int
    main: str
    description: str
    icon: str


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


@dataclass
class Wind:
    speed: float
    deg: int
    gust: Optional[int] = None


@dataclass
class Rain:
    one_hour: float = None
    three_hours: float = None


@dataclass
class Snow:
    one_hour: float = None
    three_hours: float = None


@dataclass
class Clouds:
    all: int


@dataclass
class Sys:
    type: int
    id: int
    country: str
    sunrise: int
    sunset: int
    message: str = None


@dataclass
class WeatherData:
    coord: Coord
    weather: list[Weather]
    base: str
    main: Main
    visibility: int
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
