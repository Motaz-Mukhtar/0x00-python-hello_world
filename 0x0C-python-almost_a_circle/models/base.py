#!/usr/bin/python3
# base.py
"""Define Base Class"""
import json


class Base():
    """Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Intitlize Attribute

            Args:
                id (int): id of instance class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
            of list_dictionaries

            Args:
                list_dictionaries (list): dict list
        """
        if (list_dictionaries is None or
                len(list_dictionaries) == 0):
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of
            list_objs to a file

            Args:
                list_objs (list): list of objects
        """
        filename = clas.__name__ + ".json"

        with open(filename, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
                return
            else:
                for items in list_objs:
                    json_file.write(json.dumps(items))

    @classmethod
    def from_json_string(json_string):
        """Retunrs the list of the JSON string
            representation json_string

            Args:
                json_string (str): JSON representation
        """
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)

    @staticmethod
    def create(cls, **dictionary):
        """Returns an instance with all
            attributes already set

            Args:
                dictionary (dict): dict of new attr
        """
        if cls.__name__ == "Rectangle":
            new_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances:"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as json_file:
                lis = Base.from_json_string(json_file.read())
                for items in lis:
                    cls.create(**items)
        except IOError:
            return "[]"
