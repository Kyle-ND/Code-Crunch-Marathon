import requests
from datetime import datetime
import smtplib, ssl
from dotenv import load_dotenv
import os

load_dotenv() 

context = ssl.create_default_context()

def read_sheet():
    response = requests.get('https://api.sheety.co/f6c54075ef4f6bfa569fcf5eb96e9b54/birthdayWisher/sheet1')
    content_list = response.json()
    data = content_list['sheet1']
    return data

def check_birthday_send_email(data):
    today = datetime.now().strftime("%d-%m")  # Get today's date in "dd-mm" format
    
    for entry in data:
        # Check if today matches the birthday date format "dd-mm" (excluding year)
        if entry['dateOfBirth'][:-5] == today:
            receiver = entry['email']
            message = f"""\
To: {receiver}
From: {os.getenv("SENDER_EMAIL")}
Subject: Hi There!

Today is your birthday! Happy Birthday! Do enjoy your day and make the most of it.

Peace,
Kamogelo
"""
            try:
                with smtplib.SMTP_SSL(os.getenv("SMTP_SERVER"), int(os.getenv("PORT")), context=context) as server:
                    server.login(os.getenv("SENDER_EMAIL"), os.getenv("PASSWORD"))
                    # Send email
                    server.sendmail(os.getenv("SENDER_EMAIL"), receiver, message)
                    print('Email sent successfully to', receiver)
            except Exception as e:
                print(f"Error sending email: {e}")

# Run the functions
data = read_sheet()
check_birthday_send_email(data)