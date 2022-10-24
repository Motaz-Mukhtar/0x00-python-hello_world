#!/usr/bin/python3
"""Write a Function that returns True if object inherited from class"""


def inherits_from(obj, a_class):
    return issubclass(type(hash(obj)), a_class)
