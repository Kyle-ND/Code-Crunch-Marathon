"""
A module for helper functions.
"""
from creds import (
    twilio_account_sid,
    twilio_auth_token,
    twilio_phone_number,
    user_phone_number
)
from twilio.rest import Client


def send_sms(message: str) -> dict:
    """
    Send SMS to verified number from predefined number.

    Parameters:
        message (str): Message we want to send to the user
    Return:
        response (dict): Response from the attempt to send the message
    """
    
    client = Client(twilio_account_sid, twilio_auth_token)

    message = client.messages.create(
        from_= twilio_phone_number,
        body = message,
        to = user_phone_number
    )

    return message.sid


if __name__ == "__main__":
    # Test cases
    message = "Hey, Sakhile, alien technology is here! Ayinabungozi lento."
    print(send_sms(message))