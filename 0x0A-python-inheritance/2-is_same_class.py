#!/usr/bin/python3
'''
A module for 2-is_same class
'''


def is_same_class(obj, a_class):
    '''
    a method that returns true if object is of specified class

    attributes:
    obj - the object to be checked
    a_class - the class to check
    '''
    if type(obj) is a_class:
        return True
    else:
        return False
