# sender.py
import sys

from sender_messages import send_email, send_text

AFFRIMATIVE = ['y', 'yes', 'yeah']
# Adding way to send argument from command line:
#   py sender.py -quick "Message to receiver" -r receiver_email(or number)
#                -type_of_message_flag -receiver_flag

def check_args():
    """
    Gets arguments from command line.
    """
    pass


if __name__ == '__main__':
    # use sys.argv values to make custom messages from terminal
    check_args()

    #ans = input("Would you like to send custom message? ")
    #if ans in AFFRIMATIVE:
        #receiver, message = custom_message()
        #send_email(receiver, message)

    # Test Message
    send_email()

    print("Test Message sent!")
