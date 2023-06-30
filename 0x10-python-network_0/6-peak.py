#!/usr/bin/python3
"""contains a function that finds the
peak number in an list"""

def find_peak(list_of_integers):
    """function that finds the peak in a list
    of integers"""
    if not list_of_integers:
        return None
    
    if (list_of_integers[0] >= list_of_integers[1]):
        return None

    i = 0
    j = len(list_of_integers) - 1

    while i <= j:
        middle = (i + j)

        if (middle == 0 or list_of_integers[middle] >= list_of_integers[middle - 1])
            and 

