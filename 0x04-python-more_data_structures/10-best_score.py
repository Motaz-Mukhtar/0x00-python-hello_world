#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    score = 0
    name = ""
    for i in a_dictionary:
        num = a_dictionary.get(i)
        if num > score:
            name = i
            score = num
    return name
