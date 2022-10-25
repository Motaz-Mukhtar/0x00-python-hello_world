#!/usr/bin/python3
"""Creates an Ojbect from JSON file"""
import json


def load_from_json_file(filename):
    """Createan Object from filename

        Args:
            filename (str): JSON file name
    """
    with open(filename, encoding="utf-8") as myFile:
        string = myFile.read()
        return json.loads(string)
