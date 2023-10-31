#!/usr/bin/python3
a = 0
b = 1
while a < 9:
    for b in range(1, 10):
        if int('{}{}'.format(a, b)) < 89:
            if a != b:
                print('{}{}'.format(a, b), end=', ')
        else:
                print('{}{}'.format(a, b))
    a += 1
