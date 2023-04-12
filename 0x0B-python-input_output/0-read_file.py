#!/usr/bin/python3
"""
    Contains a function that reads a text file
    and prints it to stdout
"""

def read_file(filename=""):
    """function that reads a text file
    and prints it"""
    with open("{}".format(filename), "r", encoding="utf-8") as f:
        f.read()
