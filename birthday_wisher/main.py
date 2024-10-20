import smtplib
import datetime
from email.message import EmailMessage
import requests,json

def send_email(receipient_data):
    email = EmailMessage()
    email['Subject'] = 'Happy Birthday 🎂'
    email['From'] = 'Automate test'
    email['To'] = ''
    email.set_charset('')
    
    
def get_data():
    End_point= "https://api.sheety.co/ef491bcfd06cc17c7074d5b4b6f10bbc/birthdaySheet/dateofbirths"
    
    response = requests.get(url=End_point)
    str1 = response.text
    data  = json.loads(str1)
    
    return data['dateofbirths']


#response = requests.post(url=End_point,json=user_info)
print(get_data())
# date = datetime.datetime.now()
# print(date)
