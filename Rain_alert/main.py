import os 
from dotenv import load_dotenv
import requests ,json

def get_data():
    load_dotenv()
    api_url = os.getenv('key')
    response = requests.get(url=api_url)
    data = json.loads(response.text)
    return data['weather']

def weather_condition(data):
    pass


print(get_data())