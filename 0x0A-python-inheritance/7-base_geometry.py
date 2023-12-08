#!/usr/bin/python3
'''
A 6-base_geometry module
'''


class BaseGeometry:
    '''
    A class with diffrent methods

    raises:
    Exception - if method is implemented
    '''
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
