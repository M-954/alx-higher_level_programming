#!/usr/bin/python3
def uppercase(str):
    string = ''
    for letter in str:
        if ord(letter) >= 97 and ord(letter) <= 122:
            LETTER = chr(ord(letter) - 32)
            string += LETTER
        else:
            string += letter
    print(string)
