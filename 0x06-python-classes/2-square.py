#!/usr/bin/python3
"""Define Square Class"""


class Square:
    """Initilize a new square class"""
    def __init__(self, size=0):
        """Initialize a new Square.


        Args:
            size (int): The size of new square
        """
        try:
            self.__size = size
            if size < 0:
                raise ValueError
        except TypeError:
            print("Size must be an integer")
        except ValueError:
            print("size must be >= 0")

