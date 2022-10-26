#!/usr/bin/python3
"""Define Student Class"""


class Student:
    """Student Class"""
    def __init__(self, first_name, last_name, age):
        """instanlize attributes

            Args:
                first_name (str): name
                last_name (str): name
                age (int): number
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dict representation of a student

           Args:
                attrs (list): list of attributes
            Return:
                Dictionary
        """
        if (type(attrs) == list and
                all(type(i) == str for i in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributres of Student instance

            Args:
                json (dict): values of the new attributes
        """
        for i in json:
            if hasattr(self, i) and type(json) == dict:
                setattr(self, i, json[i])
