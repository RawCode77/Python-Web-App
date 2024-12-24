from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()

def get_current_weather(city="New York"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data

"""
make a module that gets the current weather for a city
"""
if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nEnter the name of the city: ")

    weather_data = get_current_weather(city)

    print("\n")

    pprint(weather_data) 