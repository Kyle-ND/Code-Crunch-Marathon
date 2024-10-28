import requests
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Environment variables
APPS_PASSWORD = os.getenv("APPS_PASSWORD")
EMAIL = os.getenv("EMAIL")

# Constants
URL = 'https://api.sheety.co/3facb7789ccb8d6a7acf7735666d6746/birthdayWisher/sheet1'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465


def get_birthdays(url):
    """
    Fetches birthday data from the given URL.

    Args:
        url (str): The API endpoint URL to fetch birthday data.

    Returns:
        dict: The JSON response containing birthday data.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None


def extract_items_json(data):
    """
    Extracts names, emails, and birthdays from JSON data.

    Args:
        data (dict): JSON data from the API response.

    Returns:
        tuple: A tuple containing three lists - names, emails, and birthdays.
    """
    names, emails, birthdays = [], [], []

    if "sheet1" in data:
        for item in data["sheet1"]:
            names.append(item["name"])
            emails.append(item["email"])
            birthdays.append(item["birthday"][5:])  # Extract month and day

    return names, emails, birthdays


def send_email(sender, password, recipient, subject, body):
    """
    Sends an email to the specified recipient.

    Args:
        sender (str): The email address of the sender.
        password (str): The app password for the sender's email account.
        recipient (str): The email address of the recipient.
        subject (str): The subject of the email.
        body (str): The body content of the email.

    Returns:
        None
    """
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp_server:
            smtp_server.starttls()
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipient, msg.as_string())
        print(f"Message sent to {recipient}!")
    except Exception as e:
        print(f"Failed to send email: {e}")


def main():
    """
    Checks if today matches any birthday and sends an email if it does.

    Args:
        None

    Returns:
        None
    """
    current_date = datetime.now().strftime("%m-%d")  # Get current month and day

    data = get_birthdays(URL)
    if not data:
        return

    names, emails, birthdays = extract_items_json(data)

    # Iterate over birthdays to check if today matches
    for i in range(len(birthdays)):
        if birthdays[i] == current_date:
            name = names[i]
            recipient = emails[i]
            subject = f"Happy Birthday {name}!"
            body = f"Happy birthday from Top 1% WTC, {name}!"
            send_email(EMAIL, APPS_PASSWORD, recipient, subject, body)
        
    print("No Birthdays today, no e-mail's sent. ")

if __name__ == "__main__":
    main()
