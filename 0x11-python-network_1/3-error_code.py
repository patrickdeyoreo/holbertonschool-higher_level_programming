#!/usr/bin/python3
'''
Send a request to a URL and display the body of the response
'''

import sys
from urllib.error import HTTPError, URLError
from urllib.request import urlopen


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: ', __file__, 'URL', file=sys.stderr)
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as r:
            print(r.read().decode())
    except HTTPError as exc:
        print('Error code:', exc.code, file=sys.stderr)
        sys.exit(1)
    except URLError as exc:
        print('Error:', exc.reason, file=sys.stderr)
        sys.exit(1)
    except ValueError as exc:
        print('Error:', exc, file=sys.stderr)
        sys.exit(1)
