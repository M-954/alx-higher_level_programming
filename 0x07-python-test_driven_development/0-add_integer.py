#!/usr/bin/python3
"""
A module that adds two integers
"""


def add_integer(a, b=98):
    """
    A function that adds two integers a and b


    raises:
    TypeError - if a or b is not an integer or float
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return a + b
