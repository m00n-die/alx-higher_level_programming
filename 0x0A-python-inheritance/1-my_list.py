#!/usr/bin/python3
"""
    Contains a class MyList that inherits
    from list
"""

class MyList(list):
    """A class that inherits from list"""
    
    def print_sorted(self):
         """Prints sorted list"""
         print(sorted(self))