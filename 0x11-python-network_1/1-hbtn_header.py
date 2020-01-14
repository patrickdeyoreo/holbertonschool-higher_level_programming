#!/usr/bin/python3
'''
Makes a request to a URL and displays the value of the X-Request-Id header
'''

import sys
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: ', __file__, 'URL', file=sys.stderr)
        sys.exit(2)

    try:
        with urlopen(sys.argv[1]) as r:
            print(r.getheader('X-Request-Id'))
    except HTTPError as exc:
        print('Error code:', exc.code)
        sys.exit(1)
    except URLError as exc:
        print('Error:', exc.reason)
        sys.exit(1)
    except ValueError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
