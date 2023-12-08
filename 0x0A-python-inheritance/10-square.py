#!/usr/bin/python3
'''
A 9-rectangle module
'''


class BaseGeometry:
    '''
    A class with diffrent methods

    raises:
    Exception - if method is implemented
    '''
    def __init__(self):
        pass

    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''
        An integer validator method


        attributes:
        name - name given to the value
        value - value given to represent name

        raises:
        TypeError - if value is not an integer
        ValueError - if value is less than or equal to zero'''

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
        if not name and not value:
            raise TypeError("integer_validator() missing 2 required "
                            "positional arguments: 'name' and 'value'")
        if value is None:
            raise TypeError("integer_validator() missing 1 required "
                            "positional argument: 'value'")


class Rectangle(BaseGeometry):
    '''
    A class rectangle that inherits from basegeometry
    '''
    def __init__(self, width, height):
        '''
        initialization of the class rectangle


        attributes:
        self.width - the legth of the shorter side
        height: the length of the longer side


        args:
        self.width - the legth of the shorter side
        height: the length of the longer side
        '''
        super().__init__()
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Implements the area of a rectangle'''
        return (self.__width * self.__height)

    def __str__(self):
        '''
        Implements the string representation of the rectangle
        '''
        return ('[Rectangle] {}/{}'.format(self.__width, self.__height))


class Square(Rectangle):
    '''
    Implementation of a class square
    '''
    def __init__(self, size):
        '''
        the initialization of the square class


        attribute:
        size - the length of one side of a square


        returns the area of a square
        '''
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        '''
        implements the string representation of the square
        '''
        return ('[Square] {}/{}'.format(self.__size, self.__size))
