#!/usr/bin/python3
"""Define Square Class"""


class Square:
    """Initialize a New square class"""
    def __init__(self, size=0):
        """__init__ Function

        Args:
            size (int): The size of new Square
        """
        self.__size = size
    @property
    def size(self):
        """retritive Size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Initialize a new Square.


        Args:
            value (int): The size of new square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Are of the square


        Return:
            The Current square Area
        """
        return self.__size * self.__size
