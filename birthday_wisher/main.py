
#     Fetch birthdays from Google Sheets.
#     Check if today is anyone’s birthday from the database.
#     Send personalized email wishes using smtplib.
#     Simple configuration through environment variables.

# ✅ Prerequisites

#     Python 3.x installed
#     Google Account with access to a Google Sheet
#     Google Cloud Console Project with Sheets API enabled
#     Service Account credentials for Google Sheets (JSON format)
#     Email account with SMTP access (e.g., Gmail) 

import datetime
import requests

now = datetime.datetime.now()

print("Current time and Date")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

url = 'https://api.sheety.co/8e795ed44dd8f61421599f326443c4b9/birthdayWishes/sheet1'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
    # Do something with the data
    print(data['sheet1'])

else:
    
    print(f"Error: {response.status_code}")

class Birthday:

    __birthdays = []

    def __init__(self, people=[]):
        self.people = people

    def find_birthdays(self):
        for person in self.people:
            if self.is_birthday_today(person.get('birthday')):
                self.__birthdays.append(person)

        return self.__birthdays

    def is_birthday_today(self, birthday):
        birthday = (
            datetime
            .strptime(birthday, '%Y-%m-%d')
            .strftime('%d-%m')
        )

        return bool(birthday == datetime.now().strftime('%d-%m'))






