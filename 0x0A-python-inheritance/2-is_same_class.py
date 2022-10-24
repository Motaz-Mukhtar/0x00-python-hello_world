#!/usr/bin/python3
"""write a fucntion that returns True or False"""


def is_same_class(obj, a_class):
    """Returns True if the obj is exactly instance of a_class
       Otherwise False."""
    return isinstance(obj, a_class)
