#!/usr/bin/python3
"""A project onclasses and object"""


class Square:
    """A square defined class


    Attributes:
        __size: length of one side of square


    raises:
        TypeError: if size is not an integer
        ValueError: if size is less than zero


    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """
        calculates the area of a square


        Attributes:
        __size: length of one side of square


        Returns: area of square


        """
        area = self.__size ** 2
        return (area)
