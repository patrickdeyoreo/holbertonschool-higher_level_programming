#!/usr/bin/python3
'''
Makes a request and prints information about the body of the response
'''

import urllib.request

URL = 'https://intranet.hbtn.io/status'

if __name__ == '__main__':

    with urllib.request.urlopen(URL) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode())
