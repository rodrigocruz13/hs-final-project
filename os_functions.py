#!/usr/bin/python3

import os
import sys


def clear_screen():
    """
    Purpose:   Function that clear the screen according to the OS
    Arguments: - None.
    Returns:   - Nothing.
    """

    if (sys.platform != 'linux'):
        os.system('cls')  # For Windows
    else:
        os.system('clear')  # For Linux/OS X


def read_and_validate_url():
    """
    Purpose:   Function that read and argument and valitate it as URL.
    Arguments: - None.
    Returns:   - A valid URL.
    """

    validate_domain = __import__('web-scraping').validate_domain

    url = None
    while (url is None):
        address = input("Type a valid URL with the format http: ... :  ")
        url = validate_domain(address)
    return (url)


def now_stamp():
    """ Function that returns the current time in string format
    Returns:
        Current time in str format
    """

    from datetime import datetime
    # current date and time
    return str(datetime.now())
