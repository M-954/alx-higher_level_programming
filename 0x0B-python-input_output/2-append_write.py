#!/usr/bin/python3
'''
An implementation of the 2-append_write module
'''


def append_write(filename="", text=""):
    '''
    Implementation of the append file handling method
    '''
    with open(filename, "a", encoding="UTF8") as file:
        file.write(text)
        return len(text)
