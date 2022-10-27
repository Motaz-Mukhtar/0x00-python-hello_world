#!/usr/bin/python3
# 5-save_to_json_file.py
"""Defines a json file writing fucntion"""
import json


def save_to_json_file(my_obj, filename):
    """write an my_obj to a filename using JSON representation"""
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(json.dumps(my_obj))
