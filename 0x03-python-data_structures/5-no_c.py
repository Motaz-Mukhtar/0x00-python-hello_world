#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for i in my_string:
        if i == 'c' or i == 'C' or i == None:
            print("", end="")
        else:
            new_string.append(i)
    return ''.join(new_string)
print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
