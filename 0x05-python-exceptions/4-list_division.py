#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            result_list.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
        except ZeroDivisionError:
            print("division by 0")
            result_list.append(0)
        except TypeError:
            result_list.append(0)
            print("wrong type")
    return result_list
