#!/usr/bin/python3
"""
List all states from a MySQL database localhost at port 3306
"""

from mysqlman import MySQLMan
from sys import argv, exit, stderr


if __name__ == '__main__':
    try:
        params = {
            'user': argv[1],
            'password': argv[2],
            'database': argv[3],
            'host': 'localhost',
            'port': 3306,
        }
    except IndexError:
        stderr.write('Usage: {} username password database\n'.format(argv[0]))
        exit(1)
    mysqlman = MySQLMan(connect=True, **params)
    for row in mysqlman.query("SELECT id, name FROM states ORDER BY id;"):
        print(row)
