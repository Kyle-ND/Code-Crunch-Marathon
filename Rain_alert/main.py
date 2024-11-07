"""
A module to check rain forecast and arn the user through Twilio SMS
"""

from helper import (
    get_user_location,
    get_weather_data,
    send_sms
)


def main() -> None:
    """
    Main driver function for the program.

    Parameters
        None
    Return:
        None
    """
    # Get user location
    location = get_user_location()
    # Uunpack tuple to latitude and longitude
    lat, lon = location
    # Get hourly weather data 
    exclude = 'hourly'
    hourly_forcast = get_weather_data(lat, lon, exclude)
    # Process that data and formulate warning for the user
    mock_warning = "Rain in the next hour. We cannot sell ice cream today."
    # Send the user a warning SMS
    send_sms(mock_warning)


if __name__ == "__main__":
    # Start the program
    main()
