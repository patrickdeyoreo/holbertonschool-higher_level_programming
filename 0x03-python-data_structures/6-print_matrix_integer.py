#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    print(*[' '.join(['{:d}'.format(n) for n in a]) for a in matrix], sep='\n')
