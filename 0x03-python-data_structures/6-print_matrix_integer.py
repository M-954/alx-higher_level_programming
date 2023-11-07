#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for k in matrix:
        m = 1
        for j in k:
            if m == len(k):
                print("{}".format(j), end="")
            else:
                print("{}".format(j), end=" ")
            m = m + 1
        print()
