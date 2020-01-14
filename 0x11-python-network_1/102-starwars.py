#!/usr/bin/python3
'''
Take a string send a POST request to search the Star Wars API
'''

import sys
import requests

URL = 'https://swapi.co/api/people'

if __name__ == '__main__':

    params = {'search': sys.argv[1]}
    search = requests.get(URL, params=params).json()
    number = search.get('count')
    people = search.get('results')
    print('Number of results:', number)
    while search.get('next'):
        search = requests.get(search['next']).json()
        people += search.get('results')
    for person in people:
        print(person.get('name'))
        for link in person.get('films'):
            film = requests.get(link).json()
            print('\t', film.get('title'), sep='')
