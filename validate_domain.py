#!/usr/bin/python3

import requests
import sys


def validate_domain(web_address):
    """ Function that queries a web address to validate connection
    Args:
        web_address (str): url to check.
    Returns:
        A URL in correct format if available connection
        None if no connection available.
    """

    if (web_address[-1] != '/'):
        url = web_address + '/'
    else:
        url = web_address

    try:
        url_request = requests.get(url).text
        return (url)
    except requests.exceptions.RequestException as err:
        print(err)
        return (None)
