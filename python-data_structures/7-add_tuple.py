#!/usr/bin/python3
def add_tuple(tuple_a=(), tuble_b=()):
    a = tuple_a[:2]
    b = tuble_b[:2]

    a += (0,) * (2 - len(a))
    b += (0,) * (2 - len(b))

    return a[0] + b[0], a[1] + b[1]
