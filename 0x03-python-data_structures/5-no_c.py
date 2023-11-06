#!/usr/bin/python3
def no_c(my_string):
    mylist = list(my_string)
    for char in mylist:
        if char == 'c' or char == 'C':
            mylist.remove(char)
    return("".join(listofchars))
