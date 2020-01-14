#!/usr/bin/python3
'''
Send an email to a URL using a POST request and display the response body
'''

import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('Usage: ', __file__, 'URL', 'email', file=sys.stderr)
        sys.exit(1)

    REQUEST = Request(sys.argv[1], data={'email': sys.argv[2]}, method='POST')
    try:
        with urlopen(REQUEST) as r:
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
