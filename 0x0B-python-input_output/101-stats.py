#!/usr/bin/python3
""" Read lines from standard input and compute metrics
Input Format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""

from collections import defaultdict
from sys import stdin


if __name__ == '__main__':
    status_codes = defaultdict(lambda: 0)
    total_size = 0
    line_count = 0
    while True:
        try:
            *_, status_code, file_size = stdin.readline().split()
            status_codes[status_code] += 1
            total_size += int(file_size)
            if line_count < 9:
                line_count += 1
            else:
                line_count = 0
                raise KeyboardInterrupt
        except (KeyboardInterrupt, ValueError):
            print("File size: {}".format(total_size), *[
                "{}: {}".format(k, status_codes[k])
                for k in sorted(status_codes)
            ], sep="\n")
