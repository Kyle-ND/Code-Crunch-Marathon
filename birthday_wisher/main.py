import smtplib
import datetime
from email.message import EmailMessage

def send_email(receipient_data):
    email = EmailMessage()
    email['Subject'] = 'Happy Birthday 🎂'
    email['From'] = 'Automate test'
    email['To'] = ''
    email.set_charset('')
    


date = datetime.datetime.now()
print(date)
