#!/usr/bin/python3
"""

This module is composed of a function that prints 2 new lines after ".?:" characters

"""


def text_indentation(text):
    """ Function that prints 2 new lines after ".?:" characters

    Args:
        text: input string

    Returns:
        No return

    Raises:
        TypeError: If text is not a string


    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    
    cp = text[:]
    for i in ".?:":
        list_text = cp.split(i)
        cp = ""
        for j in list_text:
            j = j.strip(" ")
            cp = j + i if cp is "" else cp + "\n\n" + j + i
    print(cp[:-3], end="")