import smtplib
import datetime
from email.message import EmailMessage
import requests,json
from menu import option_sys
from dotenv import load_dotenv
import os

def send_email(person,age): #will send message via email to a certain address. 
    name = person['name']
    surname = person['surname']
    email_address = person['email']
    company_name = "C.Prime"
    message = f"""Hi {name} {surname} 💫,
Happy Birthday from {company_name}🎊! We hope you're feeling extra special today and celebrating in style🙌.
Here at {company_name}, we believe birthdays are the perfect excuse to indulge, so go ahead and eat that extra slice of cake or buy that pair of shoes you've had your eye on.

{company_name}
+27 011 235 444
prime.co.za
    """
    sender_email = os.getenv('sender_email')
    two_factor_key = os.getenv('two_factor_key')
    #email=====================
    email = EmailMessage()
    email['Subject'] = f'Happy Birthday 🎂 {name}'
    email['From'] = company_name
    email['To'] = person['email']
    email.set_content(message) #email body
    #sending=====================
    server  = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email,two_factor_key) #<---- 2 step F KEY HERE
    server.send_message(email)
    server.quit()
    
 
def get_data():

    End_point= os.getenv('End_point') 
    response = requests.get(url=End_point)
    str1 = response.text
    data  = json.loads(str1)
    
    
    return data['dateofbirths']

def add_birthday(name,surname,dateofbirth,email):
    End_point= os.getenv('End_point') 
    
    data = {
        "dateofbirth": {
            "name" : name,
            "surname" : surname,
            "dateOfBirth" : dateofbirth,
            "email": email

        }
    }

    response = requests.post(url=End_point,json=data)
    response.raise_for_status()


def main():
    load_dotenv()
    

    options = ["View Todays birthday","View ALL Birthdays","Add A Birthday (+)","Remove A Birthday (-)"] 
    while True:
        people = get_data()
        date = datetime.datetime.now()
        day,month,year = date.strftime('%d'), date.strftime('%m'), date.strftime('%Y')
        
        
        choice = option_sys(options,"============== Birthday Wisher Deshboard: ==============\n \n (press 'p' to select)\n press ENTER to move through options")
        is_a_birthday_today = False
        match choice:
            case 0:
                #=================================================================================
                print("\033[1;34m",options[choice],"\033[0;37m")
                for person in people:
                    
                    d_o_b = person['dateOfBirth'].split("/")
                    if d_o_b[0] == day and d_o_b[1] == month: #send email if today is a birthday 
                        age = int(year)-int(d_o_b[2])
                        send_email(person,age)
                        is_a_birthday_today = True
                        print("-> ",person['dateOfBirth'],person['name'])

                    

                        
                        
                if is_a_birthday_today is not True:
                    print("There is no birthday Today...🚫")
                #=================================================================================     
                
            case 1:# view all birthdays
                print("\033[1;34m",options[choice],"\033[0;37m")
                for pp in people:
                    print("-> ",pp['dateOfBirth'],pp['name'])

            case 2:# add
                print("\033[1;34m",options[choice],"\033[0;37m")
                name = input("\033[1;34mName: \033[0;37m")
                surname = input("\033[1;34mSurname: \033[0;37m")
                dateofbirth = input("\033[1;34mDOB [dd/mm/yyyy]: \033[0;37m")
                email = input("\033[1;34mEmail: \033[0;37m")
            
                add_birthday(name,surname,dateofbirth,email)
                
                pass
            case 3:#remove
                print("\033[1;34m",options[choice],"\033[0;37m")
                

                pass
        
    
        input("press ENTER to proceed...")
            

 
if __name__ == '__main__':
    main()