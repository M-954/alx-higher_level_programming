#!/usr/bin/python3
"""
Defines a locked class"""


class LockedClass():
    """class LockedClass that only allows +
    'instantiation of the attribute fisrt_class"""
    __slots__ = ["first_name"]
