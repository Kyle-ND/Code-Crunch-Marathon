import geocoder
import requests

def get_coordinates():
    g = geocoder.ip("me")

    if g.latlng is not None:
        return g.latlng
    else:
        return None


def main():
    coordinates = get_coordinates()
    if coordinates is not None:
        latitude, longitude = coordinates
    else:
        print("Unable to retrieve your GPS coordinates.")
    
    key = "0c1610760b9e94815ac1574e5980ed3a"
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&exclude=hourly,daily&appid={key}"
    response = requests.get(url).json()

    rainy = response["current"]["weather"][0]["main"]

    if rainy == "rain":
        print("Send message")
    else:
        print("Dont send message")

if __name__ == "__main__":
    main()