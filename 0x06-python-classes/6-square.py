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
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the size and position


        args:
        size(int): length of one side
        position tuple ((int), (int)): gives the horizontal and vertical position


        Raises:
        TypeError: if length is not an integer
        ValueError: if length is less than zero
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter for position


        Attributes:
        __position: the vertical offset for new line and horizontal offset for spaces


        Raises:
        TypeError: if value is not a tuple of two positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter position for the new value


        Attributes:
        __position: the vertical offset for new line and horizontal offset for spaces



        Args:
        Value: the new vertical and horizontal offsets


        Raises:
        TypeError: if value is not a tuple of two positive integers
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        for i in value:
            if type(i) is not int or i < 0:
                raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

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
        for _ in range(self.__position[1]):
                print()

        for _ in range(self.__size):
                print(" " * self.__position[0] + '#' * self.__size)
        if self.__size == 0:
            print()
