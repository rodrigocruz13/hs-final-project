#!/usr/bin/python3

import json
import re
import requests
import sys


def get_link_list(fixed_url):
    """ Gets all the valid and unique links from a fixed url.
    Args:
            fixed_url (str): Web address used to find the links.
    Returns:
            A list of unique links
            Returns None if no links can be obtained.
    """

    print('URL: {}'.format(fixed_url))
    html_response = requests.get(fixed_url).text

    links_regex = re.compile('<a\s+.*href=[\'"]?([^\'" >]+)', re.IGNORECASE)
    original_links = links_regex.findall(html_response)
    original_links.sort()

    unique_links = []
    for link in original_links:
        full_url = re.sub(r'^\.?/{1,2}', fixed_url, link, count=1)

        cid = full_url.find('?cid')
        if (cid != -1):
            full_url = full_url[0:cid]

        disq = full_url.find('#disqus_thread')
        if (disq != -1):
            full_url = full_url[0:disq]

        java = full_url.find('javascript:void(0)')
        http = full_url.find('http')
        slug = full_url.find('{')
        qton = full_url.find('?')

        repeat = 1
        if (full_url not in unique_links):
            repeat = - 1

        if (java == -1 and http != -1 and slug == -1 and repeat == -1 and qton == -1 and disq == -1):
            unique_links.append(full_url)

    unique_links.sort()
    return(unique_links)


def check_all(link_list):
    """ Checks the code status of each link
    Args:
            link_list (list): List with all the links from a web address.
    Returns:
            A list with the code status of each link
    """

    status_dict = {}
    list_lenght = len(link_list)
    print('Links obtained: \t {}'.format(list_lenght))

    i = 0
    for link in link_list:
        i += 1
        progress = i * 100 / list_lenght

        try:
            response = requests.get(link).status_code
        except:
            print('\nmmmmm')

        item_i = {}
        item_i.setdefault(link, str(response))
        key = 'Check ' + str(i).zfill(3)
        status_dict.setdefault(key, item_i)

        sys.stdout.write("Check progress: \t %.2f%%   \r" % (progress))
        sys.stdout.flush()

    return(status_dict)


def print_errors(url, status_dict):
    """ Print the list
    Args:
            url (str): Url domain
            status_list (list): List with all the links ant its errors
    Returns:
            Nothing
    """

    dict_lenght = len(status_dict)
    print('\nElements dict = {}'.format(dict_lenght))

    if (dict_lenght == 0 or status_dict == None):
        print('\nNo problems found')
        exit(1)

    semicolon = url.find(":") + 3
    com = url.find('.com')
    basename = url[semicolon: com]

    print('Name: {}.json'.format(basename))
    save_dict_to_file(status_dict, basename)

    print('\nChecked elements: \t {}\n'.format(dict_lenght))
    # print_board(status_dict)


def print_board(status_dict):
    """ Print a board with the results
    Args:
            status_list (list): List with all the links ant its errors
    Returns:
            Nothing
    """

    i = 0
    dash = '-' * 88
    for link, status in status_dict.items():
        if i == 0:
            print(dash)
            print('{:^8s}{:<125s}'.format('Status', ' Link'))
            print(dash)
        elif(status is not '200'):
            print('{:^8s}{:<125s}'.format(status, link))
        i += 1


def save_dict_to_file(dict, name):
    path = 'filestorage/'
    filename = path + name + '.json'
    f = open(filename, 'w')
    objects = json.dumps(dict, indent=4, skipkeys=True, sort_keys=True)
    f.write(objects)
    f.close()


def load_dict_from_file(name):
    path = 'filestorage/'
    filename = path + name + '.json'
    f = open(filename, 'r')
    data = f.read()
    f.close()
    return eval(data)
