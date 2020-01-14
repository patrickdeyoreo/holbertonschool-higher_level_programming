#!/usr/bin/python3
'''
Send a request to a URL and display the body of the response
'''

import requests

URL = 'https://intranet.hbtn.io/status'

if __name__ == '__main__':

    with requests.get(URL) as r:
        print("Body response:")
        print("\t- type:", type(r.text))
        print("\t- content:", r.text)
