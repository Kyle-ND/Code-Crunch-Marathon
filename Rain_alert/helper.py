"""
A module for helper functions.
"""

from creds import (
    api_key,
    twilio_account_sid,
    twilio_auth_token,
    twilio_phone_number,
    user_phone_number
)
from dotenv import load_dotenv
import requests
from requests.exceptions import HTTPError
from samples import wx_sample_response
from twilio.rest import Client


load_dotenv() # Take environment variables from .env

def get_weather_data(lat: float, lon: float, exclude: str) -> dict:
    """
    Get current weather from the given city's latitude and longitude.

    Parameters:
        lat (float): Angular distance of place north/south of equater
        lonv(float): Angular distance of place east/west of greenwich meridian
    Return:
        weather_data (dict): All weather information about the city
    """

    URL = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={exclude}&appid={OPENWEATHER_API_KEY}"
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
    

def process_weather(weather_data: dict) -> str:
    """
    Process weather from given location, give rain warning if needed

    Parameters:
        weather_data (dict): Weather information from a given location
    Return:
        weather_forecast (str): Warning to user if there is rain
    """
    warning_words = [
        "rain",
        "drizzle",
        "precipitation",
        "thunderstorms",
        "showers",
        "hail",
        "sleet",
        "snow",
        "snowflake"
    ]

    # Get weather data from the dictionary at 'data' key element 0
    dict_wx_data = weather_data['data'][0]
    # Get dictionary with weather data we are interested on
    weather_dict = dict_wx_data['weather'][0]
    # Issue the warning
    for item in weather_dict:
        for warning in warning_words:
            if type(weather_dict[item]) == int: # Skip integeer items
                continue
            else:
                if warning in weather_dict[item].lower():
                    return "Rain is expected in you area (Time Expected: 1 hour), get to shelter."
    return "Clear blue sky, go to the swimming pool"


def send_sms(message: str) -> dict:
    """
    Send SMS to verified number from predefined number.

    Parameters:
        message (str): Message we want to send to the user
    Return:
        response (dict): Response from the attempt to send the message
    """
    
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        from_= TWILIO_NUMBER,
        body = message,
        to = USER_NUMBER
    )

    return message.sid


if __name__ == "__main__":
    # Test cases
    # Test data
    # Johannesburg (lat, lon)
    # lat = -26.204103
    # lon = 28.047304
    # exclude = "hourly"
    # print(f"Hardcoded: ({lat}, {lon})")
    # print(f"Retrieval: {get_user_location()}")
    # print(get_weather_data(lat, lon, exclude))
    # message = "Hey, Sakhile, alien technology is here! Ayinabungozi lento."
    # print(send_sms(message))
    print(process_weather(wx_sample_response))