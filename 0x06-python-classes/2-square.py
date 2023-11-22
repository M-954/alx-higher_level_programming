#!/usr/bin/python3
"""A project onclasses and object"""


class Square:
    """A square defined class"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
