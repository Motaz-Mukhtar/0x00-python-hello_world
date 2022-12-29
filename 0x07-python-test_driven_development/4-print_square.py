#!/usr/bin/python3
""" Prints a square with the character #."""


def print_square(size):
    """
        Prints a square with the character #.

        Raises:
            TypeError: size must be int.
            ValueError: size must be Greater than 0.
    """
    if type(size) != int or (type(size) == float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for x in range(0, size):
            print("#", end="")
        print()
