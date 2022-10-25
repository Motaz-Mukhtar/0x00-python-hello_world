#!/usr/bin/python3
"""Appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of filename

        Args:
            filename (str): The filename
            text (str): the text
        Returns:
            The number chr of the new text
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        myFile.write(text)
        chrNum = 0
        for i in text:
            for j in i:
                chrNum += 1

    return chrNum
