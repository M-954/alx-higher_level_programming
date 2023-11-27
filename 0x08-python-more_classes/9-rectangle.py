#!/usr/bin/python3
"""Defining a class Rectangle"""


class Rectangle:
    """A Rectangle defined class


    class attribute:
    number_of_instances - keeps track of the number of instances
    print_symbol - symbol for character representation of rectangle

    Attributes:
        width (int) - length of the longer side
        height (int) - length of the shorter side

    Args:
        __width (int) - length of the longer side
        __height (int) - length of the shorter side
        """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

        self.number_of_instances = 0
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        A static method


        Attribute:
        rect_1- an instance of Rectangle
        rect_2- an instance of Rectangle

        Raises:
        TypeError: if rect_1 or rect_2 is not an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_1 >= area_2:
            return (rect_1)
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        A class method


        Returns:
        returns a new instance of class with similar lengths
        """
        return cls(size, size)

    def __str__(self):
        """Defines a public method __str__


        prints # character to represent a rectangle
        """
        rectangle_str = ""
        if self.__height == 0 or self.__width == 0:
            return rectangle_str
        if type(self.print_symbol) is list:
            print_symbol = ''.join(map(str, self.print_symbol))
        else:
            print_symbol = self.print_symbol
        for h in range(self.__height):
            for w in range(self.__width):
                rectangle_str += print_symbol
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

    def __del__(self):
        """
        A public method __del__


        prints the message "Bye rectangle..."
        """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
