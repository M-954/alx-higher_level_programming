#!/usr/bin/python3i
"""
A 5-text_indentation module
"""

def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    current_line = ""

    for c in text:
        delim = ('.', '?', ':')
        current_line += c
        if c in delim:
            print(current_line.strip())
            print()
            current_line = ""

    if current_line.strip():
        print(current_line.strip())
