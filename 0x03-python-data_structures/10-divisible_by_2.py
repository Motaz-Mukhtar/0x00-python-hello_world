#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            list_result.append(true)
        else:
            list_result.append(false)
    return list_result
