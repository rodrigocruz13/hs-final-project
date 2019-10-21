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

    url_0 = None
    while (url_0 is None):
        address = input("Type a valid URL with the format http: ... :  ")
        address.replace(' ', '')
        url_0 = validate_domain(address)

    if (url_0[4] == ':'):
        url_1 = validate_domain(url_0[0:4] + 's' + url_0[4:])
    else:
        url_1 = validate_domain(url_0[0:4] + url_0[5:])

    return ([url_0, url_1])


def now_stamp():
    """
    Purpose:   Function that returns the current time in string format.
    Arguments: - None.
    Returns:   - Current time in str format.
    """

    from datetime import datetime

    return str(datetime.now())
