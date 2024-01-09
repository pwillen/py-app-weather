from typing import Dict, List

from pydantic import BaseModel


class Coord(BaseModel):
    lon: float
    lat: float

class Weather(BaseModel):
    id: int


class WeatherData(BaseModel):
    coord: Coord
    weather: List
    base: str
    main: Dict
    visibility: int
    rain: Dict
    clouds: Dict
    dt: int
    sys: Dict
    timezone: int
    id: int
    name: str
    cod: int


