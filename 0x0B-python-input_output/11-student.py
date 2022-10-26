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
        if (type(attrs) == stra and
                all(type(i) == str for i in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        else:
            return self.__dict__
