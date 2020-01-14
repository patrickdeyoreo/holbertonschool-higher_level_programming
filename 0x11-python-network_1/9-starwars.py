#!/usr/bin/python3
'''
Take a string send a POST request to search the Star Wars API
'''

import sys
import requests

URL = 'https://swapi.co/api/people'

if __name__ == '__main__':

    resp = requests.post(URL, data={'search': sys.argv[1]})
    data = resp.json()
    print('Number of results:', data['count'])
    for result in data['results']:
        print(result['name'])
