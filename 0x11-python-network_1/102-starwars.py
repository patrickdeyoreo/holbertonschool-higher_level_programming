#!/usr/bin/python3
'''
Take a string send a POST request to search the Star Wars API
'''

import sys
import requests

URL = 'https://swapi.co/api/people'

if __name__ == '__main__':

    params = {'search': sys.argv[1]}
    people = requests.get(URL, params=params).json()
    print('Number of results:', people.get('count'))
    while people.get('results'):
        for person in people['results']:
            print(person.get('name'))
            for url in person.get('films'):
                film = requests.get(url).json()
                print('\t{}'.format(film.get('title')))
        if people.get('next'):
            people = requests.get(people['next']).json()
        else:
            break
