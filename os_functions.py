#!/usr/bin/python3

import os
import sys

validate_domain = __import__('validate_domain').validate_domain


def clear_screen():
    """ Function that clear the screen according to the OS
    Returns:
        Nothing
    """

    if (sys.platform != 'linux'):
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/OS X


def read_and_validate_url(argv):
    """ Function that read and argument and valitate it as URL
    Returns:
        The URL
    """

    if (len(argv) != 2):
        print('Usage: {} http://www.example.com/'.format(argv[0]))
        exit(1)
    url = validate_domain(argv[1])

    if (url is None):
        exit(1)
    return (url)


def now_stamp():
    """ Function that returns the current time in string format
    Returns:
        Current time in str format
    """

    from datetime import datetime
    # current date and time
    return str(datetime.now())
