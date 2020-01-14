#!/usr/bin/python3
'''
Makes a request to a URL and displays the value of the X-Request-Id header
'''

import urllib.request
import sys


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: ', __file__, 'URL', file=sys.stderr)
        sys.exit(1)

    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
