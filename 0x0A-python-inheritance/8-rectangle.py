#!/usr/bin/python3
"""Creat Rectangle Class"""
BaseGeometry = __import__('7-base_geometry.py').BaseGeometry


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
        self.integer_validato("height", height)
        self.__height = height
