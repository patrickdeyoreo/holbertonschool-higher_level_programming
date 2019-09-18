#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    return tuple(map(sum, zip(
        (*tuple_a, 0, *([0] * (not tuple_a)))[:2],
        (*tuple_b, 0, *([0] * (not tuple_b)))[:2]
    )))
