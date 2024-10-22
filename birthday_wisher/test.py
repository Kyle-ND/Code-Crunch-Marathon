import smtplib
from email.mime.text import MIMEText


subject = "Happy Birthday "
body = "This is the body of the text message"
sender = "azizmuhammadhashim6@gmail.com"
recipient = ""
password = "password"
def send_email(name, email, birthday):
    print((name, email, birthday))

def send_email(subject, body, sender, recipient, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipient)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipient, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipient, password)