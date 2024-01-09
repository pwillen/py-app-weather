import os

from dotenv import load_dotenv

from weather import WeatherClient


def main():

    load_dotenv(dotenv_path=os.path.join('..', 'dev.env'))

    city = 'Charlotte'

    weather_client = WeatherClient(
        api_key=os.getenv('OPENWEATHER_KEY')
    )
    weather_data = weather_client.get_weather(city)

    if weather_data:
        print(f"Weather in {city}:")
        print(f"Temperature: {weather_data['main']['temp']} K")
        print(f"Description: {weather_data['weather'][0]['description']}")
    else:
        print("Failed to retrieve weather data.")


if __name__ == "__main__":
    main()