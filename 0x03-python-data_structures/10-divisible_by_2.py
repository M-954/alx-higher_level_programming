#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mylist2 = []
    for digit in my_list:
        if (digit % 2) == 0:
            mylist2.append(True)
        else:
            mylist2.append(False)
    return(mylist2)
