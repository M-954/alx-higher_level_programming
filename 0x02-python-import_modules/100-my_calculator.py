#!/usr/bin/python3
import sys
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    count = len(sys.argv)
    if count != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    accepted_operator = ['+', '-', '*', '/']

    if operator not in accepted_operator:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    else:
        if operator == '+':
            result = add(a, b)
        if operator == '-':
            result = sub(a, b)
        if operator == '*':
            result = mul(a, b)
        if operator == '/':
            result = div(a, b)
    print('{} {} {} = {}'.format(a, operator, b, result))
