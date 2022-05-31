#!/usr/bin/python3
"""class inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """def class Rectangle"""

    def __init__(self, width, height):
        """init class"""
        Rectangle.integer_validator(self.__init__, "width", width)
        self.__width = width
        Rectangle.integer_validator(self.__init__, "height", height)
        self.__height = height

    def area(self):
        """calc the area of rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """Rectangle <w>/<h>"""
        return f"[Rectangle] {self.__width}/{self.__height}"
