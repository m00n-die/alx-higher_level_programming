#!/usr/bin/python3
"""
    Contains a function that writes a string
    and returns a number characters written 
"""

def append_write(filename="", text=""):
    """writes a string to a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
