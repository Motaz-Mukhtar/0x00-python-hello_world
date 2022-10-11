#!/usr/bin/python3
"""Define Square Class"""


class Square:
    """Initilize a new square class"""
    def __init__(self, size=0):
        """Initialize a new Square.


        Args:
            size (int): The size of new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Are of the square


        Return:
            The Current square Area
        """
        return self.__size * self.__size
