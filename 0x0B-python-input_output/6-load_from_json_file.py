#!/usr/bin/python3
# 6-load_from_json_file
"""Defines a JSON file reading fucntion"""
import json


def load_from_json_file(filename):
    """Create Object from JSON file"""
    with open(filename, encoding="utf-8") as myFile:
        string = myFile.read()
        return json.loads(string)
