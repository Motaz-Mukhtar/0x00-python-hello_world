#!/usr/bin/python3

def common_elements(set_1, set_2):
    set_3 = []
    for i in set_1:
        for k in set_2:
            if i == k:
                set_3.append(k)
    return set_3
