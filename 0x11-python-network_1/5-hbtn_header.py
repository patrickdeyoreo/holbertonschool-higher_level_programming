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

    try:
        with requests.get(sys.argv[1]) as r:
            print(r.headers['X-Request-Id'])
    except requests.exceptions.ConnectionError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.InvalidSchema as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.MissingSchema as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
