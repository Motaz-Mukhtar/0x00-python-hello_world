#!/usr/bin/python3
"""Define Base Class"""


class Base:
    """Base Class"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Intitlize Attribute
        
            Args:
                id (int): id of instance class
        """
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects