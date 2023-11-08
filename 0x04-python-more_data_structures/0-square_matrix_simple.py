#!/usr/bin/python3
new_matrix = []
for row in matrix:
    new_row = [item * item for item in row]
    new_matrix.append(new_row)
return new_matrix
