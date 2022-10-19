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
        self.width = width
        self.height = height

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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    def area(self):
        """Find the area of the Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
