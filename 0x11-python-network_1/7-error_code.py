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
        RESP = requests.post(sys.argv[1])
        CODE = RESP.status_code
        TEXT = RESP.text
    except requests.exceptions.RequestException as exc:
        print(exc)
        sys.exit(1)

    if CODE >= 400:
        print('Error code:', CODE)
    else:
        print(TEXT)
