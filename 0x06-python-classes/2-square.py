#!/usr/bin/python3

class Square:

    def __init__(self, size=0):
        try:
            self.__size = size
            if size < 0:
                raise ValueError
        except TypeError:
            print("Size must be an integer")
        except ValueError:
            print("size must be >= 0")

