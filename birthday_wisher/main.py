from dotenv import load_dotenv
import os
import requests
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

SERVICE_ACCOUNT_FILE = os.getenv('Google_birthday_credentials')

#Function for getting the spreadsheet
def getting_sheet():
    SPREAD_SHEET = os.getenv('SHEET_URL')
    data = requests.get(SPREAD_SHEET)

    if data.status_code == 200:
        response = data.json()
        return response['sheet1']

#Function for sending email
def sending_mail():
        EMAIL = os.getenv('EMAIL_SENDER')
        PASSWORD = os.getenv('PASSKEY_')
        today_date = datetime.now().strftime("%d/%m")

        birth_data = getting_sheet()
        print(birth_data)
        if not birth_data:
            print("No data found")

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        print("Logged in successfully")

        for person in birth_data:
            if person["dob"] == today_date:
                name = person["name"]
                to_mail = person['emailAddress']
                print("To mail: ",person['emailAddress'])
                if name and to_mail:
                    subject = (f"Happy Birthday {name}!")
                    message = (f"Go {name} it's your Birthday!\n \n"
                        "May your birthday be the start of a year filled with new opportunities, accomplishments,endless joy. "
                        "May all your birthday wishes come true except the illegal ones.\n\n"
                        "Happiest birthday!\n\n"
                        "Enjoy your day")

                full_message = MIMEMultipart()
                full_message['From'] = EMAIL
                full_message['To'] = to_mail
                full_message['Subject'] = subject
                full_message.attach(MIMEText(message, 'plain'))
                
                server.sendmail(EMAIL, to_mail, full_message.as_string())
                print(f"Email sent to {to_mail}")
                server.quit()
                print(f"Successfully sent email to {name}")

sending_mail()