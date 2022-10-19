#!/usr/bin/python3
"""Define Rectangle"""


class Rectangle:
    """Rectangle Class"""
    def __init__(self, width=0, height=0):
        """ Set The Attribute

            Args:
                width (int): width of the Rect
                height (int): height of the Rect
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width

            Args:
                value (int): the value of the width
        """
        self.__width = value

    @property
    def height(self):
        """retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ set the height

            Args:
                value (int): The value of the height
        """
        self.__height = value
