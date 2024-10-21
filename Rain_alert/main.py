import geocoder
import requests
from twilio.rest import Client

def get_coordinates():
    g = geocoder.ip("me")

    if g.latlng is not None:
        return g.latlng
    else:
        return None


def main():
    #Get coordinates
    coordinates = get_coordinates()
    if coordinates is not None:
        latitude, longitude = coordinates
    else:
        print("Unable to retrieve your GPS coordinates.")
    
    #Get weather
    key = "0c1610760b9e94815ac1574e5980ed3a"
    url = f"https://api.openweathermap.org/data/3.0/onecall?lat={latitude}&lon={longitude}&exclude=hourly,daily&appid={key}"
    response = requests.get(url).json()
    rainy = response["current"]["weather"][0]["main"]

    #Set up messaging
    account_sid = "AC11bab766d5743bbb09416e4554e8cdeb"
    auth_token = "cd067ff68d45bfb42acc45f8e1c2a7ff"
    client = Client(account_sid, auth_token)

    #Send messages
    if rainy.lower() == "rain":
        message = client.messages.create(
                body="The weather is expected to rain.",
                from_="+12096339790",
                to="+27794802246",
                )
        print(message.body)
    else:
        message = client.messages.create(
                body="The weather is not expected to rain.",
                from_="+12096339790",
                to="+27794802246",
                )
        print(message.body)

if __name__ == "__main__":
    main()