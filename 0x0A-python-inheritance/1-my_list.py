#!/usr/bin/python3
"""MyList Class"""


class MyList(list):
    """MyList that inherits from list"""
    def print_sorted(self):
        print(sorted(self))
