import os
import requests,json
from datetime import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()
# fecthing my secret_key and secret_url from my .env
SECRET_KEY = os.getenv("SECRET_KEY")
SECRET_URL = os.getenv("SECRET_URL")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")

# create a function to fecth data from the secret_url
def getdata():
    response = requests.get(url=SECRET_URL)
    text = response.text
    data  = json.loads(text)
    
    
    return data["sheet1"]

# create the main function
def email_birthday():
    today = datetime.today().strftime("%d / %m")
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(SENDER_EMAIL,SECRET_KEY)
    datas = getdata()
    print(datas)
    birthdaytoday = False
    for info in datas:
        receiver_email = info["email"]
        fullname  = info["fullname"]
        company_name = "Jason Arnold"
        message = f"""
        Happy Birthday {fullname}🎉🎂
        May your day be filled with joy, love, and laughter. Wishing you a year ahead filled with blessings, success, and happiness. 
        May God bless you abundantly today and always! 🙏✨
        
        Best Regards
        {company_name}
        """
        if info["birthday"] == today:
            msg = MIMEMultipart("body")
            msg["Subject"] = f'Happy Birthday {fullname}🎉🎂'
            msg["From"] = SENDER_EMAIL
            msg["To"] = receiver_email
            server.sendmail(SENDER_EMAIL,receiver_email,message)
            birthdaytoday = True
    if birthdaytoday != True:
        print("It is no one's birthday today")
    
    
    server.quit()
    
email_birthday()