#!/usr/bin/python3i
"""
A 5-text_indentation module
"""

def text_indentation(text):
    """
    A module that prints a text with 2 new lines
    after each of these characters: ., ? and :


    Attribute:
    text (str) - the text to be printed
    raise:
    TypeError - if text is not a string
    """
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
