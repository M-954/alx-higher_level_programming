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

    def area(self):
        """A public instance area


        Returns:
        area - the product of width and height
        """
        area = self.__width * self.__height
        return area

    def perimeter(self):
        """A public instance perimeter


        Returns:
        perimeter - the sum of width and height multiplied by 2
        """
        perimeter = 2 * (self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            perimeter = 0
        return perimeter

    def __str__(self):
        """Defines a public method __str__


        prints # character to represent a rectangle
        """
        rectangle_str = ""
        if self.__height is 0 or self.__width is 0:
            return rectangle_str
        for h in range(self.__height):
            for w in range(self.__width):
                rectangle_str += '#'
            if h != self.__height - 1:
                rectangle_str += '\n'
        return rectangle_str

    def __repr__(self):
        """
        defines a public method __repr__


        Returns:
        returns a string representation of the rectangle
        """
        return ("Rectangle({}, {})".format(self.__width, self.__height))
