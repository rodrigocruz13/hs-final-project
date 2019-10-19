#!/usr/bin/python3
import sys


if __name__ == '__main__':

    get_link_list = __import__('web-scraping').get_link_list
    check_all = __import__('web-scraping').check_all
    print_errors = __import__('web-scraping').print_errors
    clear_screen = __import__('os_functions').clear_screen
    read_and_validate_url = __import__('os_functions').read_and_validate_url

    clear_screen()
    url = read_and_validate_url(sys.argv)
    links_list = get_link_list(url)
    error_dict = check_all(links_list)
    print_errors(url, error_dict)
