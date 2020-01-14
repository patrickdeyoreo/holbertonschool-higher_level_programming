#!/usr/bin/python3
'''
Makes a request to a URL and displays the value of the X-Request-Id header
'''

import sys
import requests


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: ', __file__, 'URL', file=sys.stderr)
        sys.exit(1)

    resp = requests.get(sys.argv[1])
    print(resp.headers.get('X-Request-Id'))
