import os
import smtplib

from private import EMAIL_ADDRESS, EMAIL_PASSWORD

AFFRIMATIVE = ['y', 'yes', 'yeah']
#EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
#EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

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


if __name__ == '__main__':
    ans = input("Would you like to send custom message? ")
    if ans in AFFRIMATIVE:
        receiver, message = custom_message()
        send_email(receiver, message)

    else:
        send_email()

    print("Message sent!")
