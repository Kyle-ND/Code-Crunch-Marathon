import os 
from dotenv import load_dotenv
import requests ,json

def get_data():
    load_dotenv()
    api_url = os.getenv('key')
    response = requests.get(url=api_url)
    return response.text

def weather_condition(data):
    pass


get_data()