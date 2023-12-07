#!/usr/bin/python3
'''
A 4-inherits_from module
'''


def inherits_from(obj, a_class):
    '''
    A method that returns true if object is instance '
    'of class that inherited from given class

    attribute:
    obj - the given object
    a_class - the class to confirm
    '''
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
