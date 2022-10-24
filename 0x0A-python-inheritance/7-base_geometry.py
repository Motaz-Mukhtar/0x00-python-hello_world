#!/usr/bin/python3
"""Creat BaseGeometry Class"""


class BaseGeometry:
    """BaseGeometry Class"""
    def area(self):
        """Rase Exception with a message"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be an integer".format(name))
