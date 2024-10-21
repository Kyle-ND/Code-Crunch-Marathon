import smtplib
import datetime
from email.message import EmailMessage
import requests,json
from menu import option_sys

def send_email(person,age): #will send message via email to a certain address. 
    name = person['name']
    surname = person['surname']
    email_address = person['email']
    company_name = "C.Prime"
    message = f"""Hi {name} {surname} 💫,
Happy Birthday from {company_name}🎊! We hope you're feeling extra special today and celebrating in style🙌. Here at {company_name}, we believe birthdays are the perfect excuse to indulge, so go ahead and eat that extra slice of cake or buy that pair of shoes you've had your eye on.

{company_name}
+27 011 235 444
prime.co.za
    """

    #email=====================
    email = EmailMessage()
    email['Subject'] = f'Happy Birthday 🎂 {name}'
    email['From'] = company_name
    email['To'] = person['email']
    email.set_content(message)
    
    server  = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("testauston.dev@gmail.com",'#######') #<---- 2 step F KEY HERE
    server.send_message(email)
    server.quit()
    
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
    
    options = ["View Todays birthday","View ALL Birthdays","Add A Birthday (+)","Remove A Birthday (-)"] 
    while True:
        choice = option_sys(options,"============== Birthday Wisher Deshboard: ==============\n \n (press 'p' to select)\n press ENTER to move through options")
        is_a_birthday_today = False
        match choice:
            case 0:
                print("\033[1;34m",options[choice],"\033[0;37m")
                for person in people:
                    
                    d_o_b = person['dateOfBirth'].split("/")
                    if d_o_b[0] == day and d_o_b[1] == month: #
                        age = int(year)-int(d_o_b[2])
                        send_email(person,age)
                        is_a_birthday_today = True
                        
                
            case 1:
                print("\033[1;34m",options[choice],"\033[0;37m")
                for pp in people:
                    print("-> ",pp['dateOfBirth'],pp['name'])

            case 2:
                print("\033[1;34m",options[choice],"\033[0;37m")
                pass
            case 3:
                print("\033[1;34m",options[choice],"\033[0;37m")
                
                pass
        
        input("")
            

 
if __name__ == '__main__':
    main()
