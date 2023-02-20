#!/usr/bin/python3
""" Prints a text with the 2 new lines """


def text_indentation(text):
    """ Prints text and 2 new lines after each
        of these characters . ? and :

        Raises:
            TypeError: must be string
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    my_list = text.split(' ')

    for j in my_list:
        if j.endswith(":") or j.endswith("?") or j.endswith("."):
            print(j, end="")
        else:
            print(j, end=" ")
        for char in j:
            if char == '.' or char == '?' or char == ':':
                print('\n')
