# sender.py
import sys
from argparse import ArgumentParser

from sender_messages import determine_message_option

#AFFRIMATIVE = ['y', 'yes', 'yeah']

def get_args():
    """
    Get arguments from command line.

    :return: Dictionary of argument options and their values
    """
    parser = ArgumentParser()
    parser.add_argument('-m', '--message', nargs='*',
                        help='Quick Message: Send messages to self from commandline.')
    parser.add_argument('-r', '--receiver', nargs='*',
                        help='Receiver contact information goes after flag.')

    args = vars(parser.parse_args())
    return args


if __name__ == '__main__':
    # use sys.argv values to make custom messages from terminal
    args = get_args()
    determine_message_option(args)
