#!/usr/bin/python3
def no_c(my_string):
    my_string.remove('c')
    my_string.remove('C')
    return my_string
print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
