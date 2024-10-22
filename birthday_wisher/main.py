import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import smtplib

#def send_email(name, email):


def main():
    #Get spread sheet
    load_dotenv()
    end_point = os.getenv("SHEETY_END_POINT")
    response = requests.get(end_point).json()["sheet1"]

    #Get current date
    current_date = datetime.now()
    month = current_date.month
    day = current_date.day
    date = f"{day}/{month}"

    for person in response:
        name = person["name"]
        email = person["email"]
        dob= person["dob"]

        if dob == date:
            print("Send email")
        else:
            print("Dont send email")

if __name__ == "__main__":
    main()