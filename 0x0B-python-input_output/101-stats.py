#!/usr/bin/python3
""" Read lines from standard input and compute metrics
Input Format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""

from collections import defaultdict
from sys import stdin, exit as sysexit


def print_stats(file_size, status_codes):
    print("File size: {}".format(total_size), *(
        "{}: {}".format(k, status_codes[k]) for k in sorted(status_codes)
    ), sep="\n")


if __name__ == '__main__':
    status_codes = defaultdict(lambda: 0)
    total_size = 0
    line_count = 0
    while True:
        try:
            for _ in range(10):
                line = stdin.readline()
                if line:
                    *_, status_code, file_size = line.split()
                    status_codes[status_code] += 1
                    total_size += int(file_size)
                else:
                    sysexit(0)
            print_stats(file_size, status_codes)
        except KeyboardInterrupt as exc:
            print_stats(file_size, status_codes)
            raise exc
