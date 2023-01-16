#!/usr/bin/python3
# Finds a peak in a list of unsorted integers.


def find_peak(list_of_integer=[]):
    """ Return the peak number in the list """
    my_list = list_of_integer
    i = 0
    length = len(list_of_integer)
    if len(list_of_integer) == 0:
        return None

    while i < len(my_list) - 1:
        j = 0
        while j < len(my_list) - 1:
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
            j += 1
        i += 1

    if length % 2 == 1 or length == 1:
        return list_of_integer[length - 1]
    else:
        if length % list_of_integer[length - 1] == 0:
            return list_of_integer[length - 1]
        else:
            return list_of_integer[length - 2]
