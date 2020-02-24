#!/usr/bin/python3
'''
Search Twitter
'''

from sys import argv
from base64 import b64decode, b64encode
from requests import Session

URLs = {
    'token': 'https://api.twitter.com/oauth2/token',
    'search': 'https://api.twitter.com/1.1/search/tweets.json',
}

if __name__ == '__main__':

    oauth_consumer_key, oauth_consumer_secret = argv[1:2]
    auth = {
        'url': 'https://api.twitter.com/oauth2/token',
        'data': {'grant_type': 'client_credentials'},
        'headers': {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Authorization': 'Basic {}'.format(
                b64encode(':'.join([, argv[2]]).encode())
            ),
        },
    }

    with Session() as session:
        r = session.post(auth['url'], headers=auth['headers'], data=auth['data'])
        print(r.content)
