#!/usr/bin/python3
"""classes"""


class Rectangle:
    """define the rectangle class"""
    def __init__(self, height=0, width=0):
       self.height = height
       self.width = width

    @property
    def width(self):
        """retrieve width"""
        return self.width

    @width.setter
    def width(self, value):
        """set width"""
        if type(value) is not int:
            raise TypeError("widht must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return self.height

    @height.setter
    def height(self, value):
        """set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
