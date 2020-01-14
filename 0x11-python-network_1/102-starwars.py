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
    while people:
        for person in people.get('results'):
            print(person.get('name'))
            for link in person.get('films'):
                print('\t{}'.format(requests.get(link).json().get('title')))
        if people.get('next'):
            people = requests.get(people.get('next')).json()
        else:
            people = None
