#!/usr/bin/python3
'''
Send an email to a URL using a POST request and display the response body
'''

import sys
import requests


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('Usage: ', __file__, 'URL', 'email', file=sys.stderr)
        sys.exit(1)

    try:
        with requests.post(sys.argv[1], data={'email': sys.argv[2]}) as r:
            print(r.text)
    except requests.exceptions.ConnectionError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.InvalidSchema as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
    except requests.exceptions.MissingSchema as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
