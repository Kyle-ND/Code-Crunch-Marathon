import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD  =os.getenv("PASSWORD")
EMAIL =  os.getenv("EMAIL")

def get_birthdays(url):
    try:
        response = requests.get(url)

        response.raise_for_status()

        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occured: {http_err}")

    except Exception as err:
        print(f"An error occured: {err}")


url = 'https://api.sheety.co/3facb7789ccb8d6a7acf7735666d6746/birthdayWisher/sheet1';


def extract_items_json(data):
    print(data.keys())
    sheet = data["sheet1"]
    names = []
    emails = []
    birthdays = []
    print(sheet)

    # Corrected loop
    for item in sheet:
        names.append(item["name"])
        emails.append(item["email"])
        birthdays.append(item["birthday"][5:])

    return names, emails, birthdays

def send_email(name, recipient, birthday, subject, body, sender, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipient, msg.as_string())
    print("Message sent!")


def main():

    current_datetime = datetime.now()

    current_date = str(current_datetime.date())

    current_date_split = current_date[5:]

    print(current_date_split)
    data =  get_birthdays(url)
    names, emails, birthdays = extract_items_json(data)
    name = ""
    recipient = ""
    birthday = ""
    subject = f"Happy Birthday"
    body = "This is the body of the text message"
    sender = EMAIL
    password = PASSWORD

    for i in range(len(data) + 1):
        print(birthdays[i])
        if birthdays[i] == str(current_date_split):
            name = names[i]
            recipient  = emails[i]
            birthday = birthdays[i]
            send_email(name, recipient, birthday, subject, body, sender, password)




if __name__ == "__main__":
    main()