#!/usr/bin/python3
"""Square Class"""
Rectangle = __improt__('9-Rectangle').Rectangle


class Square(Rectangle):
    """Creae Square class that inherted
        from Rectangle"""
    def __init__(self, size):
        """Initilize attr

            Args:
                size (int): size of Rectangle
        """
        self.integer_validator(size)
        self.__size = size

    def area(self):
        """Get The area of the Rectangle"""
        return self.__size * self.__size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
