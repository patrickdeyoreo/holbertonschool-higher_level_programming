#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    print(*map("{} {} {}".format, *matrix), sep='\n')
