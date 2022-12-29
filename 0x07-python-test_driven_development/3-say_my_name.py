#!/usr/bin/python3
""" Prints Name """


def say_my_name(first_name, last_name=""):
    if type(first_name) == str and type(last_name) == str:
        print("My name is {} {}".format(first_name, last_name))
    elif type(first_name) != str:
        raise TypeError("first_name must be a string")
    else:
        raise TypeError("last_name must be a string")
