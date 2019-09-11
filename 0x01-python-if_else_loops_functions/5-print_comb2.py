#!/usr/bin/python3
print(*("{:02d}".format(i) for i in range(100)), sep=', ')
