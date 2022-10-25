#!/usr/bin/python3
"""Returns an object represented by JSON string"""
import json


def from_json_string(my_str):
    """Represented by JSON string

        Args:
            my_str (str): JSON string
    """
    return json.loads(my_str)
