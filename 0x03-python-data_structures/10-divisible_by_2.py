#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    if my_list:
        return list(map(lambda n: not (n % 2), my_list))
    return None
