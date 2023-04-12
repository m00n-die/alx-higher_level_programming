#!/usr/bin/python3
"""
    Contains a function that checks if an object
    and class are of the same instance 
"""

def is_same_class(obj, a_class):
    """checks whether obj and a_class are same"""
    if isinstance(obj, a_class) == True:
        return True
    else:
        return False
    

a = 1
if is_same_class(a, int):
    print("{} is an instance of the class {}".format(a, int.__name__))
if is_same_class(a, float):
    print("{} is an instance of the class {}".format(a, float.__name__))
if is_same_class(a, object):
    print("{} is an instance of the class {}".format(a, object.__name__))