#!/usr/bin/python3
"""adds all arguments to python list"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

try:
    myList = load_from_json_file("add_item.json")
except FileNotFoundError:
    myList = []

for i in sys.argv:
    if i == sys.argv[0]:
        continue
    myList.append(i)

save_to_json_file(myList, 'add_item.json')
