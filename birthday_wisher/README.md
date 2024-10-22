# 🎉 Birthday Wisher - README

**Birthday Wisher** automates the process of checking for upcoming birthdays and sending personalized emails. This project integrates with **Google Sheets API** to fetch birthdays and uses **smtplib** to send birthday wishes via email.

---

## 📋 Table of Contents  
- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Configuration](#configuration)  
- [Usage](#usage)  
- [To-Do](#to-do)  
- [Contributing](#contributing)  
- [License](#license)

---

## ⚡ Features  
- Fetch birthdays from **Google Sheets**.  
- Check if today is anyone’s birthday from the database.  
- Send **personalized email wishes** using **smtplib**.  
- Simple configuration through environment variables.

---

## ✅ Prerequisites  

1. **Python 3.x** installed  
2. **Google Account** with access to a Google Sheet  
3. **Google Cloud Console Project** with Sheets API enabled  
4. **Service Account** credentials for Google Sheets (JSON format)  
5. Email account with **SMTP access** (e.g., Gmail)
Quickstarts explain how to set up and run an app that calls a Google Workspace API.

Google Workspace quickstarts use the API client libraries to handle some details of the authentication and authorization flow. We recommend that you use the client libraries for your own apps. This quickstart uses a simplified authentication approach that is appropriate for a testing environment. For a production environment, we recommend learning about authentication and authorization before choosing the access credentials that are appropriate for your app.

Create a Python command-line application that makes requests to the Google Sheets API.

Objectives
Set up your environment.
Install the client library.
Set up the sample.
Run the sample.
Prerequisites
To run this quickstart, you need the following prerequisites:

Python 3.10.7 or greater
The pip package management tool
A Google Cloud project.
A Google Account.
Set up your environment
To complete this quickstart, set up your environment.

Enable the API
Before using Google APIs, you need to turn them on in a Google Cloud project. You can turn on one or more APIs in a single Google Cloud project.
In the Google Cloud console, enable the Google Sheets API.

Enable the API

Configure the OAuth consent screen
If you're using a new Google Cloud project to complete this quickstart, configure the OAuth consent screen and add yourself as a test user. If you've already completed this step for your Cloud project, skip to the next section.

In the Google Cloud console, go to Menu menu > APIs & Services > OAuth consent screen.
Go to OAuth consent screen

For User type select Internal, then click Create.
Complete the app registration form, then click Save and Continue.
For now, you can skip adding scopes and click Save and Continue. In the future, when you create an app for use outside of your Google Workspace organization, you must change the User type to External, and then, add the authorization scopes that your app requires.

Review your app registration summary. To make changes, click Edit. If the app registration looks OK, click Back to Dashboard.
Authorize credentials for a desktop application
To authenticate end users and access user data in your app, you need to create one or more OAuth 2.0 Client IDs. A client ID is used to identify a single app to Google's OAuth servers. If your app runs on multiple platforms, you must create a separate client ID for each platform.
In the Google Cloud console, go to Menu menu > APIs & Services > Credentials.
Go to Credentials

Click Create Credentials > OAuth client ID.
Click Application type > Desktop app.
In the Name field, type a name for the credential. This name is only shown in the Google Cloud console.
Click Create. The OAuth client created screen appears, showing your new Client ID and Client secret.
Click OK. The newly created credential appears under OAuth 2.0 Client IDs.
Save the downloaded JSON file as credentials.json, and move the file to your working directory.
Install the Google client library
Install the Google client library for Python:


pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
Configure the sample
In your working directory, create a file named quickstart.py.
Include the following code in quickstart.py:

sheets/quickstart/quickstart.pyView on GitHub

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"
SAMPLE_RANGE_NAME = "Class Data!A2:E"


def main():
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])

    if not values:
      print("No data found.")
      return

    print("Name, Major:")
    for row in values:
      # Print columns A and E, which correspond to indices 0 and 4.
      print(f"{row[0]}, {row[4]}")
  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()
Run the sample
In your working directory, build and run the sample:


python3 quickstart.py
The first time you run the sample, it prompts you to authorize access:
If you're not already signed in to your Google Account, sign in when prompted. If you're signed in to multiple accounts, select one account to use for authorization.
Click Accept.
Your Python application runs and calls the Google Sheets API.

Authorization information is stored in the file system, so the next time you run the sample code, you aren't prompted for authorization.


---
