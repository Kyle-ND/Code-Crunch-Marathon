"""
A module to check rain forecast and arn the user through Twilio SMS
"""

from creds import api_key
import requests
from requests.exceptions import HTTPError


def get_weather_data(lat: float, lon: float, exclude: str) -> dict:
    """
    Get current weather from the given city's latitude and longitude.

    Parameters:
        lat (float): Angular distance of place north/south of equater
        lonv(float): Angular distance of place east/west of greenwich meridian
    Return:
        weather_data (dict): All weather information about the city
    """

    URL = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={api_key}"
    test_url = "https://api.github.com"

    #f"api.openweathermap.org/data/2.5/weather?q=London,uk&APPID={api_key}"
    
    # Catch any errors that may arise trying to GET the Weather data
    try:
        response = requests.get(URL)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP Error occured: {http_err}")
    except Exception as e:
        print(f"Other error occured: {e}")
    else:
        return response.json() # If request was a success


def get_user_location() -> tuple[str, str]:
    """
    Get current user location and return coordinates (lat, lon)

    Parameters:
        None
    Return:
        location (tuple): Location of user in latitude and longitude
    """

    url = "https://ipinfo.io/"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP Error occured: {http_err}")
    except Exception as e:
        print(f"Other error occured: {e}")
    else:
        json_format = response.json() # Make response into json for referencing
        location_str = tuple(json_format['loc'].split(",")) # Get lat, long, make them a tuple
        # Convert the str location to a float and give it back
        return tuple(map(float, location_str)) 


if __name__ == "__main__":
    # Test data
    # Johannesburg (lat, lon)
    lat = -26.204103
    lon = 28.047304
    exclude = "hourly"
    print(f"Hardcoded: ({lat}, {lon})")
    print(f"Retrieval: {get_user_location()}")
    # print(get_weather_data(lat, lon, exclude))
