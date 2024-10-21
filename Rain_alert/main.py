#import geocoder
import requests

# def get_coordinates():
#     g = geocoder.ip("me")

#     if g.latlng is not None:
#         return g.latlng
#     else:
#         return None


def main():
    # coordinates = get_coordinates()
    # if coordinates is not None:
    #     latitude, longitude = coordinates
    # else:
    #     print("Unable to retrieve your GPS coordinates.")
    
    key = "c61cc657a57e7c94cb7c0f3dc790a008"
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&exclude=hourly,daily&appid={key}"
    response = requests.get(url).json()
    rainy = response["current"]["rain"]

    print(response)

if __name__ == "__main__":
    main()