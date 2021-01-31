Sender

Project Goal: Send messages for the user.

Currently:
    Sends emails from terminal (use '\\' to send one '\')

To Run:
    py sender.py

  Message Flag:
      py sender.py -m 'Message to receiver'
      py sender.py --message 'Message to receiver'

  Receiver Flag:
        py sender.py -r receiver_email@mail.com
        py sender.py --receiver receiver_email@mail.com

  Message & Receiver Flags:
        py sender.py -m 'This is an email for receiver!' -r receiver_email@mail.com


Future milestones:
    Send text messages to phone from computer.
    Send automated alerts to phone/email about user's interests.
    Send delayed messages for reminders.
