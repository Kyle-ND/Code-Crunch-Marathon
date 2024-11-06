"""
A module to check rain forecast and arn the user through Twilio SMS
"""

from creds import api_key
import requests


def get_weather_data(lat: float, lon: float) -> None:
    """
    Get current weather from the given city's latitude and longitude.

    Parameters:
        lat (float): Angular distance of place north/south of equater
        lonv(float): Angular distance of place east/west of greenwich meridian
    Return:
        weather_data (dict): All weather information about the city
    """
    URL = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}"

    response = requests.get(URL)
