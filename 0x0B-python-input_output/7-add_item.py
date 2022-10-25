#!/usr/bin/python3
"""adds all arguments to python list"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

myList = []

try:
    with open('add_item.json', encoding="utf-8") as myFile:
        myList = json.loads(myFile.read())
except FileNotFoundError:
    pass

for i in sys.argv:
    if i == sys.argv[0]:
        continue
    myList.append(i)

save_to_json_file(myList, 'add_item.json')
load_from_json_file('add_item.json')
