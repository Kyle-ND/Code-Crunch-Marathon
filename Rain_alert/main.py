import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv() 

api_key = os.environ["API_KEY"]
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

def weather_by_location(): 
    current_location = input("Enter your current location (e.g., 'Cape Town' or 'Cape Town, ZA'): ")

    url = f'http://api.openweathermap.org/data/2.5/forecast?q={current_location}&appid={api_key}&units=metric'
    
    response = requests.get(url)

    data = response.json()

    return data

def check_for_rain(data):
        for forecast in data['list']:
            time = forecast['dt_txt']
            date = time[:10]
            format_time = time[-8:]
            
            rain_probability = forecast.get('pop', 0)  # Probability of precipitation (0 to 1)
            rain_probability_percentage = rain_probability * 100  # Convert to percentage    
            
            if int(rain_probability_percentage) >= 10:
                 message = client.messages.create( from_='+12567829791',
                        body = f"Hello, rain is expected on {date} at {format_time}. Please plan accordingly.",
                        to='+27605807931')
                 print('SMS sent successfully: ', message.sid)
            else:
                 print("No significant rain expected; no SMS sent.")
                 
data = weather_by_location()
check_for_rain(data)