#!/usr/bin/python3
'''
Send an email to a URL using a POST request and display the response body
'''

import sys
import requests


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('Usage: ', __file__, 'URL', 'email', file=sys.stderr)
        sys.exit(1)

    try:
        DATA = {'email': sys.argv[2]}
        TEXT = requests.post(sys.argv[1], data=DATA).text
    except requests.exceptions.RequestException as exc:
        print(exc)
        sys.exit(1)

    print(TEXT)
