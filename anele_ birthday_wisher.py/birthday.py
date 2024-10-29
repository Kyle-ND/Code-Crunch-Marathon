import os
import smtplib
from email.mime.text import MIMEText
import datetime
import requests,json
from dotenv import load_dotenv


load_dotenv()


def fetch_data():
    
    ENDPOINT = os.getenv('ENDPOINT')
    response = requests.get(url=ENDPOINT)
    dictionary_in_text =response.text
    data = json.loads(dictionary_in_text)
    return data





















