#!/usr/bin/python3
"""add two integers."""


def add_integer(a, b=98):
    """Return the summation of two integers"""
    if not type(a) == int or not type(a) == float:
        raise TypeError("a must be an integer")
    if not type(b) == int or not type(b) == float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
