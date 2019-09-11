#!/usr/bin/python3


def fizzbuzz():
    """ Do fizzbuzz in a single statement """
    print(' '.join([(i % 3 is 0) * 'Fizz'
                    + (i % 5 is 0) * 'Buzz'
                    + (str(i) if i % 3 and i % 5 else "")
                    for i in range(101)]), end=" ")
