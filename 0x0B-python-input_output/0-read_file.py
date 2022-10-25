#!/usr/bin/python3
"""Reads a text file"""


def read_file(filename=""):
    """Read the text file content

        Args:
            filename (str): text file name
    """
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read())
