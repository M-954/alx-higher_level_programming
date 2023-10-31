#!/usr/bin/python3
a = 0
while a < 9:
    for b in range(a + 1, 10):
        if int('{}{}'.format(a, b)) < 89:
            print('{}{}'.format(a, b), end=', ')
        else:
            print('{}{}'.format(a, b))
    a += 1
