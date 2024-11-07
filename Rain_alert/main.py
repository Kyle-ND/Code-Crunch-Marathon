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
    pass


if __name__ == "__main__":
    # Test data
    # Johannesburg (lat, lon)
    lat = -26.204103
    lon = 28.047304
    exclude = "hourly"
    print(f"Hardcoded: ({lat}, {lon})")
    print(f"Retrieval: {get_user_location()}")
    # print(get_weather_data(lat, lon, exclude))
