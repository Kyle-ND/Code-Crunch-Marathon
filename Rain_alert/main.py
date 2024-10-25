import os 
from dotenv import load_dotenv
import requests ,json
from twilio.rest import Client

def get_data(location): #location is a list of size two, containin lattitude and longitude coordinates
    
    load_dotenv()
    API_key = os.getenv('key')
    lat = location[0]
    lon = location[1]
    api_url =f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}' 
    response = requests.get(url=api_url)
    data = json.loads(response.text)    'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}'

    return data['weather']

def sms(content,to_number):# sends an sms to the to_number
    load_dotenv()
    account_sid = os.getenv('account_sid')
    auth_token = os.getenv('auth_token')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    messaging_service_sid=os.getenv('messaging_service_sid'),
    body=content,
    to=to_number
    )

def main():
    pass
#sms("weather","+27696608792")
print(get_data())