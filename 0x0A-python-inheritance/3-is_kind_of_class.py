#!/usr/bin/python3
'''
A 3_is_kind_of_class module
'''


def is_kind_of_class(obj, a_class):
    '''
    A method that returns true if object is an instance '
    'of a given class or subclass

    attribute:
    obj - the given object
    a_class - the class to confirm
    '''
    if isinstance(obj, a_class):
        return True
    else:
        return False
