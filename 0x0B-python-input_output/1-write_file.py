#!/usr/bin/python3
"""writes a string to a text file"""


def write_file(filename="", text=""):
    """writes text into a text file
    
        Args:
            filename (str): text file name
            text (str): the text that write
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
        chrNum = myFile.tell()
    return chrNum
