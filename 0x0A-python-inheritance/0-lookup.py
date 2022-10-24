#!/usr/bin/python3
"""available attributes and methods"""


def lookup(obj):
    """Returns the list of available attributes and methods"""
    return list(dir(obj))
