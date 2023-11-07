#!/usr/bin/python3
def no_c(my_string):
    mylist = list(my_string)
    newlist = []
    for char in mylist:
        if char != 'c' or char != 'C':
            newlist.append(char)
    return("".join(newlist))
