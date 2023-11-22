#!/usr/bin/python3
"""A project on classes and objects"""


class Square:
    """
    A class defined as square


    Attributes:
    __size: the length of one side


    Raises:
    TypeError: if length is not an integer
    ValueError: if length is less than zero
    """
    def __init__(self, size=0):
        """
        Initializes the size


        args:
        size(int): length of one side


        Raises:
        TypeError: if length is not an integer
        ValueError: if length is less than zero
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def size(self):
        """
        Getter method for the size attribute



        Returns:
        int: length of one side
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Setter method for size


        Args:
        Value: new set length


        Raises:
        TypeError: if length is not an integer
        ValueError: if length is less than zero
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """
        A public instance that calculates area of square



        Returns:
        Area of square
        """
        area = self.__size ** 2
        return (area)

    def my_print(self):
        """
        Prints representation of square using # character


        Attribute:
        __size(int): length of one side
        """
        i = 0
        while i < self.__size:
            print('#' * self.__size)
            i += 1
        if self.__size == 0:
            print()
