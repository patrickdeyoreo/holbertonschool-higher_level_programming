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

    resp = requests.get(sys.argv[1])

    if resp.status_code >= 400:
        print('Error code:', resp.status_code)
    else:
        print(resp.text)
