#!/usr/bin/python3
"""
    Contains a function that writes a string
    and returns a number characters written 
"""

def append_write(filename="", text=""):
    with open("{}".format(filename), "w", encoding="utf-8") as f:
        f.write(text)
