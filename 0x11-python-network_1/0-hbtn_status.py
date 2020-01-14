#!/usr/bin/python3
'''
Makes a request and prints information about the body of the response
'''

from urllib.request import urlopen

URL = 'https://intranet.hbtn.io/status'

if __name__ == '__main__':

    with urlopen(URL) as r:
        BODY = r.read()
        print("Body response:")
        print("\t- type:", type(BODY))
        print("\t- content:", BODY)
        print("\t- utf8 content:", BODY.decode())
