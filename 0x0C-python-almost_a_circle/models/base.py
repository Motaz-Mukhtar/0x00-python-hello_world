#!/usr/bin/python3
# base.py
"""Define Base Class"""
import json
from rectangle import Rectangle

class Base():
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

    def to_json_string(list_dictionaries):
        """returns the JSON string representation
            of list_dictionaries

            Args:
                list_dictionaries (list): dict list
        """
        if (list_dictionaries == None or
            len(list_dictionaries) == 0):
            return "[]"
        else:
            return json.dumps(list_dictionaries)
    def save_to_file(cls, list_objs):
        

