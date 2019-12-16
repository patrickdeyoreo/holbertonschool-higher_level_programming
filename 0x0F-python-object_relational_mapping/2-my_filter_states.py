#!/usr/bin/python3
"""
List all states matching given name from a MySQL db on localhost at port 3306
"""

from mysqlman import MySQLMan
from sys import argv


if __name__ == '__main__':
    params = {
        'user': argv[1],
        'password': argv[2],
        'database': argv[3],
        'host': 'localhost',
        'port': 3306,
    }
    mysqlman = MySQLMan(connect=True, **params)
    q = "SELECT id, name FROM states WHERE name = '{}' ORDER BY id;".format(
        argv[4]
    )
    results = mysqlman.query([q, ()])[0]
    for row in results:
        print(row)
