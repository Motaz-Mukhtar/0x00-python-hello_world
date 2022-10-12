#!/usr/bin/python3
"""Define Square Class"""


class Square:
    """Initialize a New square class"""
    def __init__(self, size=0, position=(0, 0)):
        """__init__ Function
        Args:
            size (int): The size of new Square
        """
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """retrieve position"""
        return self.__position

    @property
    def size(self):
        """retritive Size"""
        return self.__size

    @position.setter
    def position(self, value):
        """Initialize a new position for the Square"""
        if (not isinstance(value, tuple) or
            not all(isinstance(num, int) for num in value) or
            not all(num >= 0 for num in value) or
            len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    def size(self, value):
        self.__size = value
        """Initialize a new size for the Square.
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

    def my_print(self):
        """prints in stdout the square with the character (#)"""
        if self.__size == 0:
            print("")
        else:
            print("")
            for i in range(self.__size):
                for k in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")

