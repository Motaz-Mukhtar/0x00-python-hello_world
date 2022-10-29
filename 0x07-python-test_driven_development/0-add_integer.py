#!/usr/bin/python3
"""add two integers."""


def add_integer(a, b=98):
    """Return the summation of two integers

    Raises:
        TypeError: if either of a or b not
            int or float
    """
    if ((not isinstance(a, int) and not isinstance(b, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
