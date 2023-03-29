#1/usr/bin/python3
"""Defines a square"""

class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args: size - represnets the size of the square defined
        """

    if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
    

    
    self.__size = size
