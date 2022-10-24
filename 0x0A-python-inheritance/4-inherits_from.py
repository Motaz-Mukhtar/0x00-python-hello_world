#!/usr/bin/python3
"""Write a Function that returns True if object inherited from class
    Otherwise False"""


def inherits_from(obj, a_class):
    return issubclass(hash(type(obj)), a_class)
