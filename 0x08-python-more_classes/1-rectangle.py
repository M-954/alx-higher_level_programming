#!/usr/bin/python3
"""Defining a class Rectangle"""


class Rectangle:
    """A Rectangle defined class


    Attributes:
        width (int) - length of the longer side
        height (int) - length of the shorter side
    Args:
        __width (int) - length of the longer side
        __height (int) - length of the shorter side
        """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """The getter module for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """The setter module for width


        Attribute:
        value - the new width
        Raises:
        TypeError - if width is not an integer
        ValueError - if width is less than zero
        """

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """The getter module for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """The setter module for height


        Attributes:
        value (int) - the new value for height
        Raises:
        TypeError - if height is not an integer
        ValueError - if height is less than zero
        """

        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
