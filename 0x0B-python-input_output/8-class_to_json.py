#!/usr/bin/python3
"""Retunrs the dictionary description"""


def class_to_json(obj):
    """Returns dictionary Description
       of the obj instance

        Args:
            obj (object): instance
        Returns:
            dict Description.
    """
    return obj.__dict__
