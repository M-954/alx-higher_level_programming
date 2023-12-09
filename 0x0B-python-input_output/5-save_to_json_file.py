#!/usr/bin/python3
'''
An implementation of the 5-save_to_json_file module
'''


import json


def save_to_json_file(my_obj, filename):
    '''
    writes an object file to a text file usinf json representation
    '''
    with open(filename, "w") as json_file:
        json.dump(my_obj, json_file)
