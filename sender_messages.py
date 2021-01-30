# sender_messages.py
"""
Two methods of send messaging to self:
    Email
    Text (practically the same as email)

File has the functions to accomplish the different methods.
"""
import os
import smtplib

# Gets email and email password from private file
from private import EMAIL_ADDRESS, EMAIL_PASSWORD

def test_message():
    """
    :return: Simple email message template string
    """
    subject = 'Test Email'
    body = 'This is a test email for my python script.'
    message = f'Subject: {subject}\n\n{body}'

    return message

def custom_message():
    """
    :return: List containing receiver and message
    """
    receiver = input("Input message recipient: ")
    subject = input("Input message subject: ")
    body = input("Input message body: ")
    message = f'Subject: {subject}\n\n{body}'

    return [receiver, message]

def quick_message(receiver=None, body=None):
    """
    Asks for receiver then body input (if not specified in command line).
    :return: List containing receiver and message
    """
    subject = "Quick Message"

    if not receiver:
        receiver = input("Input message recipient: ")

    if not body:
        body = input("Input message body: ")

    message = f'Subject: {subject}\n\n{body}'

    return [receiver, message]


def receiver_number(number, carrier):
    """
    Combines number and email extension for different cell phone carriers.

    :return: String containing number and extension
    """
    pass

def send_text(receiver, message=test_message()):
    """
    Sends messages through gmail service to phone number.
    Default message is test message.
    
    :return: None
    """
    pass

def send_email(receiver=EMAIL_ADDRESS, message=test_message()):
    """
    Sends messages through gmail service.
    The default values are for the test message sent to user.

    :return: None
    """
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        #smtp.sendmail(SENDER, RECEIVER, MESSAGE)
        smtp.sendmail(EMAIL_ADDRESS, receiver, message)
