import json
import os

import requests
from dotenv import load_dotenv

from datatypes.openwather_response import WeatherData


class WeatherClient(object):
    def __init__(
        self,
        api_key: str
    ):

        self.__api_key = api_key

    def get_weather(self, city):
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': city,
            'appid': self.__api_key,
        }

        response = requests.get(base_url, params=params)

        test = json.loads(response.text)

        if response.status_code == 200:
            weather_data = WeatherData.model_validate_json(response.text)
            return weather_data
        else:
            print(f"Error: {response.status_code}")
            return None



