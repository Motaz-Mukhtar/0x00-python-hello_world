#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    i = 0
    while i < len(my_list) - 1:
        j = 0
        while j <= i:
            if my_list[i] > my_list[i + 1]:
                temp = my_list[i]
                my_list[i] = my_list[i + 1]
                my_list[i + 1] = temp
            j += 1
        i += 1
    max_num = my_list[len(my_list) - 1]
    return max_num
