#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers. """


def find_peak(list_of_integer=[]):
    """ Return the peak number in the list """
    my_list = list_of_integer.sort()
    i = 0
    length = len(list_of_integer)
    if len(list_of_integer) == 0:
        return None

    if length % 2 == 1 or length == 1:
        return list_of_integer[length - 1]
    else:
        if length % list_of_integer[length - 1] == 0:
            return list_of_integer[length - 1]
        else:
            return list_of_integer[length - 2]
