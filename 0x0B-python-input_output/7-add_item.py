#!/usr/bin/python3
"""adds all arguments to JSON list"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    myList = load_from_json_file("add_item.json")
except FileNotFoundError:
    myList = []

    myList.extend(sys.argv[1:])

save_to_json_file(myList, 'add_item.json')
