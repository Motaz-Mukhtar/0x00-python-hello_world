#!/usr/bin/python3
"""write a fucntion that returns True or False"""


def is_kind_of_class(obj, a_class):
    """Returns True if the obj is exactly instance of inherited from a_class
       Otherwise False."""
    return isinstance(obj, a_class)
