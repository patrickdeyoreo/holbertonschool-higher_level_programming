#!/usr/bin/python3
'''
Send an email to a URL using a POST request
'''

import sys
import requests


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: ', __file__, 'URL', file=sys.stderr)
        sys.exit(1)

    try:
        RESPONSE = requests.post(sys.argv[1])
    except requests.exceptions.RequestException as exc:
        print(exc)
        sys.exit(1)

    if RESPONSE.status_code >= 400:
        print('Error code:', RESPONSE.status_code)
    else:
        print(RESPONSE.text)
