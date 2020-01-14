#!/usr/bin/python3
'''
Take a string send a POST request to search the Star Wars API
'''

import sys
import requests

URL = 'https://swapi.co/api/people'

if __name__ == '__main__':

    params = {'search': '' if len(sys.argv) == 1 else sys.argv[1]}
    resp = requests.post(URL, params=params)
    data = resp.json()
    print('Number of results:', data.get('count'))
    results = data.get('results')
    while results:
        for result in results:
            print(result.get('name'))
        if data.get('next'):
            resp = requests.get(data.get('next'))
            data = resp.json()
            results = data.get('results')
        else:
            results = None
