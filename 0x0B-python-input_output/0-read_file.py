#!/usr/bin/python3
'''
An implementation of the 0-read_file module
'''


def read_file(filename=""):
    '''
    Implementation of the read file handling method
    '''
    with open(filename, "r", encoding="UTF8") as file:
        print(file.read())
