#!/usr/bin/pythonn3
'''
A 6-base_geometry module
'''


class BaseGeometry:
    '''
    A class that returns an exception when the method is called

    raises:
    Exception - if method is implemented
    '''
    def area(self):
        raise Exception('area() is not implemented')
