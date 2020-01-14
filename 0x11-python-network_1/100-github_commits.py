#!/usr/bin/python3
'''
List 10 commits (newest to oldest) of the repo "rails" by the user "rails"
'''

import sys
import requests

URLFMT = 'https://api.github.com/repos/{owner}/{repo}/commits'

if __name__ == '__main__':
    response = requests.get(URLFMT.format(repo=sys.argv[1], owner=sys.argv[2]))
    for item in response.json()[:10]:
        print('{}: {}'.format(item['sha'], item['commit']['author']['name']))
