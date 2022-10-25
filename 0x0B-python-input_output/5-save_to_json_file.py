#!/usr/bin/python3
"""writes an Ojbect to a text file"""
import json


def save_to_json_file(my_obj, filename):
    """write an my_obj to a filename
       using JSON representation

       Args:
       my_obj(str): JSON String
       filename (str): the text file
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(json.dumps(my_obj))
