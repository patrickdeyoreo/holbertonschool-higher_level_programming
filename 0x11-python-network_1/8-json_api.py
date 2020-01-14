#!/usr/bin/python3
'''
Take a letter and send a POST request to http://0.0.0.0:5000/search_user
'''

import sys
import requests

URL = 'http://0.0.0.0:5000/search_user'

if __name__ == '__main__':

    resp = requests.post(URL, data={'' if len(sys.argv) == 1 else sys.argv[1]})
    try:
        json = resp.json()
    except JSONDecodeError:
        print('Not a valid JSON')
    else:
        if json:
            print('No result')
        else:
            print('Not a valid JSON')
