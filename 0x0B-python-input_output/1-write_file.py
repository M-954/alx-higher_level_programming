#!/usr/bin/python3
'''
An implementation of the 1-write_file module
'''


def write_file(filename="", text=""):
    '''
    Implementation of the write file handling method
    '''
    with open(filename, "w", encoding="UTF8") as file:
        file.write(text)
        return len(text)
