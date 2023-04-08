#!/usr/bin/python3
"""

This module is composed of a function thad adds two integers

"""


def add_integer(a, b=98):
    """ Function that adds two integers
    
    Args:
        a: first integer
        b: second integer
    
    Returns:
        The sum of the two given integers
    
    Raises:
        TypeError: If a or b aren't integers or floats
    
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)