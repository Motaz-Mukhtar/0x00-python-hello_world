#!/usr/bin/python3
"""Write a Function that returns True if object inherited from class"""


def inherits_from(obj, a_class):
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
