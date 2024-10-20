import smtplib
import datetime
from email.message import EmailMessage
import requests,json

def send_email(person,year): #will send message via email to a certain address. 
    name = person['name']
    surname = person['surname']
    email_address = person['email']
    #email=====================
    email = EmailMessage()
    email['Subject'] = 'Happy Birthday 🎂'
    email['From'] = 'Automate test'
    email['To'] = ''
    email.set_content('')
    
    
def get_data():
    End_point= "https://api.sheety.co/ef491bcfd06cc17c7074d5b4b6f10bbc/birthdaySheet/dateofbirths"
    
    response = requests.get(url=End_point)
    str1 = response.text
    data  = json.loads(str1)
    
    return data['dateofbirths']



def main():
    
    people = get_data()
    date = datetime.datetime.now()
    day,month,year = date.strftime('%d'), date.strftime('%m'), date.strftime('%Y')
    
    print(type(day))
    for person in people:
        d_o_b = person['dateOfBirth'].split("/")
        if d_o_b[0] == day and d_o_b[1] == month: #
            send_email(person,year)
        else:
            pass
        

 
if __name__ == '__main__':
    main()
