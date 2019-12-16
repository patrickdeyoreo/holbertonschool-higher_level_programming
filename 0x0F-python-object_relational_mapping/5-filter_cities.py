#!/usr/bin/python3
"""
List all states matching given name from a MySQL db on localhost at port 3306
"""

from MySQLdb import Error
from mysqlman import MySQLMan
from sys import argv, exit, stderr


USAGE = '{} username password database search'.format(argv[0])


if __name__ == '__main__':
    try:
        params = {
            'user': argv[1],
            'password': argv[2],
            'database': argv[3],
            'host': 'localhost',
            'port': 3306
        }
        search = argv[4]
    except IndexError:
        stderr.write('usage: {}\n'.format(USAGE))
        exit(2)
    try:
        mysqlman = MySQLMan(connect=True, **params)
    except Error as e:
        stderr.write('{}\n'.format(e.args[1]))
        exit(1)
    query = """
    SELECT c.name
    FROM cities c, states s
    WHERE c.state_id = s.id
    AND s.name = %s
    ORDER BY c.id;
    """
    results = mysqlman.query([query, (search,)])
    print(', '.join(row[0] for row in results[0]))
