#!/usr/bin/python3
'''
An implementation of the 4-from_json_string module
'''


import json


def from_json_string(my_str):
    '''
    converts a json string to a python object
    '''
    return json.loads(my_str)
