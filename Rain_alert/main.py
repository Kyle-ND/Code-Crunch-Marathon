import requests
import geocoder
from dotenv import load_dotenv
from twilio.rest import Client
import os

load_dotenv()
# fecthing everything from my .env
SECRET_KEY = os.getenv("SECRET_KEY")
SECRET_URL = os.getenv("SECRET_URL")
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
MESSAGING_SERVICE_SID = os.getenv("MESSAGING_SERVICE_SID")
# To fecth user City so i can use it to get the weather info on that city and it is for my device only.
def get_city():
    g = geocoder.ip('me')
    if g.city is not None:
        return g.city
    else:
        return None
# create a function to fecth data from the that user city we just got now
def get_data():
    city = get_city()
    completed_url = API_URL + "appid=" + API_KEY + "&q=" + city
    response = requests.get(completed_url)
    info = response.json()
    return info
# create a function to get name of city, maximum temp, minimum temp, main of the weather and the description of the weather main.
def result():
    info = get_data()
    if info["cod"] != 404:
        city_name = info['name']
        x = info['main']
        maximum_temp = round(x['temp_max'] - 273.15)
        minimum_temp = round(x['temp_min'] - 273.15)
        y = info['weather']
        main_weather = y[0]['main']
        description = y[0]['description']
        return f' The city: {city_name} \n The maximun temperature in celsius: {maximum_temp}°C \n The minimun temperature in celsius: {minimum_temp}°C \n The main of the weather: {main_weather} \n The description: {description}'
    else:
        return " City Not Found "
# Create the main function to send result to sms with twilio.
def main():
    content = result()
    phone = '+27716467174'
    client = Client(ACCOUNT_SID,AUTH_TOKEN)
    message = client.messages.create(
        messaging_service_sid = MESSAGING_SERVICE_SID,
        body = content,
        to = phone)
    return message
# calling the main function.
main()

