#!/usr/bin/python3
"""

This module is composed of a function that divides the numbers of a matrix

"""


def matrix_divided(matrix, div):
    """ Function that divides the integer or float of a matrix
    
    Args:
        matrix: list of a lists of integers or floats
        div: number which divides the matrix
    
    Returns:
        A new matrix with the result of the division
    
    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers or floats
                   If div is not an integer or float
                   If the lists of the matrix don't have the same size
        
        ZeroDivisionError: If div is zero
    
    """

    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not matrix or not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    length = 0
    for items in matrix:
        if not items or not isinstance(items, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if length != 0 and len(items) != length:
            raise TypeError("Each row of the matrix must have the same size")

        for num in items:
            if not type(num) in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        length = len(items)

    res = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return (res)