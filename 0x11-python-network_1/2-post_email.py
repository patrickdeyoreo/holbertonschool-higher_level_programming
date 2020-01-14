#!/usr/bin/python3
'''
Send an email to a URL using a POST request and display the response body
'''

import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('Usage: ', __file__, 'URL', 'email', file=sys.stderr)
        sys.exit(1)

    DATA = urlencode({'email': sys.argv[2]}).encode()
    try:
        with urlopen(DATA, sys.argv[1]) as r:
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
