#!/usr/bin/python3
'''
List 10 commits (newest to oldest) of the repo "rails" by the user "rails"
'''

import sys
import requests

URL = 'https://api.github.com/repos/rails/rails/commits'

if __name__ == '__main__':
    resp = requests.get(URL)
    for item in response.json()[:10]:
        print('{}: {}'.format(item['sha'], item['commit']['author']['name']))
