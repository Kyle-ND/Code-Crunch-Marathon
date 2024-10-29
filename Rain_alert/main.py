from dotenv import load_dotenv
import os
import requests
from twilio.rest import Client


load_dotenv()

Twilio_acc_sid = os.getenv('TWILIO_ACCOUNT_SID')
Twilio_auth_token = os.getenv('TWILIO_AUTH_TOKEN')
Twilio_number = os.getenv('TWILIO_PHONE_NUMBER')
User_phone_number = os.getenv('PHONE_NUMBER')

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
City_ = os.getenv('City')
Country_Code = os.getenv('Country')

def weather():
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={City_},{Country_Code} &appid={OPENWEATHER_API_KEY}'
    response = requests.get(weather_url)
    data = response.json()

    weather_conditions = data.get("weather", [])
    for condition in weather_conditions:
        if "rain" in condition.get("main", "").lower():
            return True
    return False

def sms_alert():
    client = Client(Twilio_acc_sid, Twilio_auth_token)
    message = client.messages.create(
    from_ = Twilio_number,
    to = User_phone_number,
    body = "It won't rain today. Have a clear sky day 🙃"
    )

    print(f"SMS sent with SID: {message.sid}")

if __name__ == "__main__":
    if weather():
        sms_alert()
    else:
        sms_alert()