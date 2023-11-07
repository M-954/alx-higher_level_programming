#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for b in matrix:
        a = 1
        for c in b:
            if a == len(b):
                print("{:d}".format(c), end="")
            else:
                print("{:d}".format(c), end=" ")
            a = a + 1
        print("")
