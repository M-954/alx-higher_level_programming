#!/usr/bin/python3
from sys import stderr


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except:  # noqa
        print("Exception: Unknown format code 'd' for object of type 'str'",
              file=stderr)
        return False
