#!/usr/bin/python3
'''
Send an email to a URL using a POST request
'''

import urllib.request
import sys


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('Usage: ', __file__, 'URL', 'email', file=sys.stderr)
        sys.exit(1)

    data = {'email': sys.argv[2]}
    request = urllib.request.Request(sys.argv[1], data=data, method='POST')
    with urllib.request.urlopen(request) as response:
        print(response.getheader('X-Request-Id'))
