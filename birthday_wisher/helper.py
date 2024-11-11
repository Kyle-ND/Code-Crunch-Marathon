"""
A helper module for helper funcions.
"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials


def read_spreadsheet() -> list[list]:
    """
    Authenticat and read a Google Sheet using gspread

    Parameters:
        None
    Return:
        values (list): Values in a spreadsheet
    """
    # Define the scope for the Sheets API and Google Drive API
    SCOPES = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
    ]
    # Use the credentials file from Google Cloud Console
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json", SCOPES
    )

    # Authenticate using credentials and create client
    gc = gspread.authorize(credentials)
    spreadsheet = gc.open("Birthday Spreadsheet")

    worksheet = spreadsheet.get_worksheet(0)  # Get first sheet

    # Read values from sheet
    values = worksheet.get_all_values()

    return values
