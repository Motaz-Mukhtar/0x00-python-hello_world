#!/usr/bin/python3
my_list = [1,2,3,4,5]
idx = 5

def element_at(my_list, idx):
	if idx < 0:
		return "None"
	if idx > len(my_list) - 1:
		return "None"
	print("Element at index {} is {}".format(idx, my_list[idx]))
element_at(my_list, idx)
