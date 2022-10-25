#!/usr/bin/python3
"""MyInt Class"""


class MyInt(int):
    """Create MyInt Class"""
    def __init__(self, x):
        """Inititlized attr
            Args:
                x (int): integer type
        """
        self.__x = x

    def __eq__(self, y)
        return self.__x != y

    def __ne__(self, y):
        return self.__x == y
