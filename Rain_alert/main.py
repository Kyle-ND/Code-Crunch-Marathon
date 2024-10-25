import os 
from dotenv import load_dotenv
import requests ,json
from twilio.rest import Client

def get_data():
    load_dotenv()
    api_url = os.getenv('key')
    response = requests.get(url=api_url)
    data = json.loads(response.text)
    return data['weather']

def sms(content,to_number):
    load_dotenv()
    account_sid = os.getenv('account_sid')
    auth_token = os.getenv('auth_token')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
    messaging_service_sid=os.getenv('messaging_service_sid'),
    body=content,
    to=to_number
    )


#print(get_data())
sms("weather","+27696608792")