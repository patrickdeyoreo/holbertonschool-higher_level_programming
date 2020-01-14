#!/usr/bin/python3
'''
Take a string send a POST request to search the Star Wars API
'''

import sys
import requests

URL = 'https://swapi.co/api/people'

if __name__ == '__main__':

    params = {'search': '' if len(sys.argv) == 1 else sys.argv[1]}
    people = requests.post(URL, params=params).json()
    print('Number of results:', people.get('count'))
    while people.get('results'):
        for person in people['results']:
            print(person.get('name'))
            for url in person.get('films'):
                film = requests.get(url).json()
                print('\t', film.get('title'), sep='')
        if data.get('next'):
            data = requests.get(data['next']).json()
        else:
            break
