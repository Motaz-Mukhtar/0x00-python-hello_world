#!/usr/bin/python3
"""Creat Rectangle Class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class Inherted from BaseGeometry class"""
    def __init__(self, width, height):
        """initslize function

            Args:
                width (int): width of Rectangle
                height (int) height of Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        String = "[" + str(self.__class__.__name__) + "] "
        String += str(self.__width) + "/" + str(self.__height)
        return String
