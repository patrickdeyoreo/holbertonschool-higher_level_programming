#!/usr/bin/python3
"""Add all arguments to a list and save its JSON encoding to a file"""

from sys import argv
from json.decoder import JSONDecodeError

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

FILENAME = 'add_item.json'

if __name__ == '__main__':
    try:
        ls = load_from_json_file(FILENAME)
    except (FileNotFoundError, JSONDecodeError):
        ls = []
    ls += argv[1:]
    save_to_json_file(ls, FILENAME)
