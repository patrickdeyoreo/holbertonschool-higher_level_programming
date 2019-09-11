#!/usr/bin/python3
print('{}'.format('\n'.join(
    map(' = '.join, zip(map(str, range(99)), map('{:#x}'.format, range(99))))
)))
