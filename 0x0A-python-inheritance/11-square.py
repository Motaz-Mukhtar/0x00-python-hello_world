#!/usr/bin/python3
"""Square Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Creae Square class that inherted
        from Rectangle"""
    def __init__(self, size):
        """Initilize attr

            Args:
                size (int): size of Rectangle
        """
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)
