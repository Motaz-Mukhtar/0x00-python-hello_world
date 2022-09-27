#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = 0
    if isinstance(my_list, list):
        my_list.reverse()
    while length < len(my_list):
        print("{:d}".format(my_list[length]))
        length += 1
