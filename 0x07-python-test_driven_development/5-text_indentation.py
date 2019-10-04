#!/usr/bin/python3
"""Provides a function 'text_indentation' that formats text"""


def text_indentation(text):
    """Format text by splitting lines at special characters"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for special in '.:?':
        text = (special + '\n\n').join(
            map(lambda s: s.strip(), text.split(special + ' '))
        )
    print(text, end='')
