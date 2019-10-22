#!/usr/bin/python3

if __name__ == '__main__':

    clear_screen = __import__('os_functions').clear_screen
    read_and_validate_url = __import__('os_functions').read_and_validate_url
    get_link_list = __import__('web-scraping').get_link_list
    check_all = __import__('web-scraping').check_all
    print_results = __import__('web-scraping').print_results

    opt = 'b'
    while (opt == 'b' or opt == 'B'):
        clear_screen()
        url = read_and_validate_url()
        links_list = get_link_list(url)
        result_filename = check_all(url, links_list)
        opt = print_results(result_filename)
        print(opt)
