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
from private import EMAIL_ADDRESS, EMAIL_PASSWORD, PHONE_ADDRESS

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

def quick_send(message):
    """
    Constructs Quick Message Template

    :return: None
    """
    subject = 'Quick Message'
    quick_message = f'Subject: {subject}\n\n{message}'
    send_text(quick_message)
    return


def determine_message_method(message, receiver=None):
    """
    Determines how to send a message.

    Default: quick_send()
        no receiver then use Quick Message Template

    Try to send message as text first.
    Then try to send message as email.
        (will add custom messages to this later)

    :return: None
    """
    # Default
    if not receiver:
        # send message to self
        quick_send(message)
        return None

    try:
        number = int(receiver)
        send_text(message, receiver)

    except ValueError:
        #print(f'Receiver: {receiver} is not a number.')
        send_email(message, receiver)
    return None

def input_carrier(extensions):
    """
    Gives options for carrier extensions.
    Asks for user's input for carrier

    :return: String containing user input (carrier)
    """
    print('Pick one of these carriers: ')
    for key in extensions:
        print(f'\t{key}')

    carrier = input('carrier: ')
    return carrier

def find_closest_extension(key, extensions):
    """
    Finds closest match for carrier extension.
    If carrier not included in dictionary,
     then return the extension for first key value.

    :return: String containing carrier extension
    """
    for dict_key in extensions:
        if dict_key[0] == key[0]:
            return extensions[dict_key]
    return extensions[list(extensions.keys())[0]]

def get_receiver_extension(number):
    """
    Combines number and email extension for different cell phone carriers.

    :return: String containing number and carrier email extension
    """
    carrier_extensions = {'att':'txt.att.net',
                          'verizon':'vtext.com',
                          'sprint':'messaging.sprintpcs.com',
                          't-mobile':'tmomail.net'}
    carrier = input_carrier(carrier_extensions)
    try:
        number_contact = f'{number}@{carrier_extensions[carrier]}'

    except KeyError as key:
        ext = find_closest_extension(key.__str__(), carrier_extensions)
        number_contact = f'{number}@{ext}'

    finally:
        return number_contact


def send_text(message=test_message(), receiver=PHONE_ADDRESS):
    """
    Sends messages through gmail service to phone number.
    Default message is a test message sent to self.

    :return: None
    """
    if receiver is not PHONE_ADDRESS:
        receiver = get_receiver_extension(receiver)

    send_email(message, receiver)
    return None


def send_email(message=test_message(), receiver=EMAIL_ADDRESS):
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
    return None
