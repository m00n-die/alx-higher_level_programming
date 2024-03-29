#!/usr/bin/python3
"""A class that defines a rectangle"""

class Rectangle:
    """represents a rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing the rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """prints a message for every deleted object"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
        
    @property
    def width(self):
        """"returns width attribute"""
        return self.__width
    @width.setter
    def width(self, value):
        """"sets width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """returns height attribute"""
        return self.__height
    @height.setter
    def height(self, value):
        """"sets height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        """presents a diagram of the rectangle defined for an object"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        """returns string representation of the class"""
        return "Rectangle("+ str(self.__width) +", "+ str(self.__height) +")"
