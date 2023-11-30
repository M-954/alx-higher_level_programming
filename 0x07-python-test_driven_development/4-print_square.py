#!/usr/bin/python3
"""
A 4-print_square module
"""


def print_square(size):
    """
    A method that prints a square qith # characters


    Attributes:
    size (int) - length of one side


    Raises:
    TypeError - if size is not an integer
    ValueError - if size is less than zero
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for row in range(size):
        for column in range(size):
            print('{}'.format('#'), end="")
        print()
