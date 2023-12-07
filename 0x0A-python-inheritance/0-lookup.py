#!/usr/bin/python3
'''
A 0-lookup module
'''


def lookup(obj):
    '''
    A method that returns a list of attributes and methods
    '''
    return dir(obj)
