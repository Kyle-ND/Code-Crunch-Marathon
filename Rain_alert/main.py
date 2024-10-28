import geocoder
from geopy.geocoders import Nominatim
import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

def get_current_gps_coordinates():
    """
    Retrieves the current GPS coordinates based on the user's IP address.

    Returns:
        tuple or None: A tuple containing (latitude, longitude) if available, otherwise None.
    """
    try:
        g = geocoder.ip('me')
        if g.latlng:
            return g.latlng
    except Exception as e:
        print(f"Error retrieving GPS coordinates: {e}")
    return None

def process_coordinates(latitude, longitude):
    """
    Processes the GPS coordinates to get a human-readable location name.

    Args:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.

    Returns:
        str or None: A string with the location name if successful, otherwise None.
    """
    try:
        geo_location = Nominatim(user_agent="GetLoc")
        location_name = geo_location.reverse(f"{latitude}, {longitude}")
        print(f"Location Name: {location_name}")
    except Exception as e:
        print(f"Error retrieving location name: {e}")

def get_weather_by_location(latitude, longitude):
    """
    Fetches the current weather information based on latitude and longitude.

    Args:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.

    Returns:
        str or None: The main weather description (e.g., 'Clear', 'Clouds') if successful, otherwise None.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_json = response.json().get("weather", [])
        if weather_json:
            current_weather = weather_json[0].get("main", "Unknown")
            return current_weather
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
    return None

def send_sms(current_weather):
    """
    Sends an SMS with the current weather information.

    Args:
        current_weather (str): A brief description of the current weather.

    Returns:
        None
    """
    try:
        message = client.messages.create(
            body=f"The current weather for today is {current_weather}",
            from_="+12562865821",
            to="+27785703745"
        )
        print(f"Message sent: {message.body}")
    except Exception as e:
        print(f"Error sending SMS: {e}")

def main():
    """
    Main function to get GPS coordinates, fetch location and weather, and send an SMS with weather information.

    Returns:
        None
    """
    coordinates = get_current_gps_coordinates()
    if coordinates:
        latitude, longitude = coordinates
        print("Your current GPS coordinates are:")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")
        process_coordinates(latitude, longitude)
        
        current_weather = get_weather_by_location(latitude, longitude)
        if current_weather:
            send_sms(current_weather)
        else:
            print("Unable to retrieve weather information.")
    else:
        print("Unable to retrieve your GPS coordinates.")

if __name__ == "__main__":
    main()
