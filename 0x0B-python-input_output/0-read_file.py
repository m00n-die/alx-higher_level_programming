#!/usr/bin/python3
"""
    Contains a function that reads a text file
    and prints it to stdout
"""

def read_file(filename=""):
    """function that reads a text file
    and prints it"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
