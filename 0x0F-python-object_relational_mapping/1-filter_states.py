#!/usr/bin/python3
"""
List all states starting with 'N' from a MySQL db on localhost at port 3306
"""

from MySQLdb._exceptions import OperationalError
from mysqlman import MySQLMan
from sys import argv, exit, stderr


USAGE = '{} username password database'.format(argv[0])


if __name__ == '__main__':
    try:
        mysqlman = MySQLMan(
            connect=True,
            user=argv[1],
            password=argv[2],
            database=argv[3],
            host='localhost',
            port=3306
        )
    except IndexError:
        stderr.write('usage: {}\n'.format(USAGE))
        exit(2)
    except (OperationalError, ProgrammingError) as e:
        stderr.write('{}\n'.format(e.args[1]))
        exit(1)
    query = "SELECT id, name FROM states ORDER BY id;"
    results = mysqlman.query([query, ()])
    for row in results[0]:
        if row[1].startswith('N'):
            print(row)
