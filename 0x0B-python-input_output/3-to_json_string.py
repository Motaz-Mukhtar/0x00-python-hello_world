#!/usr/bin/python3
"""Returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """ representation of an object

        Args:
            my_obj (any): object
    """
    return json.dumps(my_obj)
