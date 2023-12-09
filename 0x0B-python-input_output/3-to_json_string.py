#!/usr/bin/python3
'''
An implementation of the 3-to_json_string module
'''


import json


def to_json_string(my_obj):
    '''
    converts a python object to a json string
    '''
    return json.dumps(my_obj)
