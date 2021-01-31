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


def combine_strings(string_list):
    """
    Combine string_list's values into a new string
     with spaces inserted between list values.

    :return: string
    """
    if isinstance(string_list, list):
        new_string = ''
        insert_spaces(string_list)
        for item in string_list:
            new_string += item
        return new_string
    return string_list

def insert_spaces(string_list):
    """
    Inserts whitespace inbetween words in list.

    :return: None
    """
    num_spaces = len(string_list) - 1
    for i in range(num_spaces):
        # insert spaces into odd indexes
        index = 2*i + 1
        string_list.insert(index, ' ')
    return None

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
    Constructs Custom Message Template

    :return: None
    """
    receiver = input("Input message recipient: ")
    # no receiver inputted --> send to self
    if not receiver:
        subject = 'Quick Message'
    else:
        subject = input("Input message subject: ")

    body = input("Input message body: ")
    message = f'Subject: {subject}\n\n{body}'
    send_email(message)

    #arg_dict = {'receiver':receiver, 'message':message}
    #determine_message_option(arg_dict)
    return None

def quick_send(message):
    """
    Constructs Quick Message Template

    send_text() not working as intended.
    send_email() used for now.

    :return: None
    """
    subject = 'Quick Message'
    quick_message = f'Subject: {subject}\n\n{message}'
    #send_text(quick_message)
    send_email(quick_message)
    return None

def determine_message_option(arg_dict):
    """
    Determines which message template to use using arg_dict.
    arg_dict = {'message': value(s),
                'receiver': value(s)
    }

    Four Options:
        1. quick_send(message)
            - no receiver means message to self (Quick Message Template)
        2. custom_message()
            - no message and no receiver (Custom Message Template)
        3. send_text(message, receiver)
            - receiver must be a number (phone number check later)
        4. send_email(message, receiver)
            - sends message as email as last option

    :return: None
    """
    message = arg_dict['message']
    receiver = arg_dict['receiver']

    # converts message value into a string
    message = combine_strings(message)
    receiver = combine_strings(receiver)

    # send message to self with Quick Message Template
    if message and not receiver:
        quick_send(message)
        return None

    # input information into Custom Message Template
    elif not message and not receiver:
        custom_message()
        return None

    # message and receiver is supplied
    # test to determine if receiver is a number
    try:
        number = int(receiver)
        send_text(message, receiver) # not working as intended

    except ValueError:
        send_email(message, receiver)
    return None

def input_carrier(extensions):
    """
    Gives options for carrier extensions.
    User inputs a carrier

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
        # checks if carrier is included in dictionary
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

    **Currently, send_text is not working as intended.
        - every message is sent through a different contact on phone.
        - long delay between sent and delivery.

    :return: None
    """
    # PHONE_ADDRESS number that is saved to file
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
        # starts communication with email server
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        #smtp.sendmail(SENDER, RECEIVER, MESSAGE)
        smtp.sendmail(EMAIL_ADDRESS, receiver, message)
    print('Message sent!')
    return None
