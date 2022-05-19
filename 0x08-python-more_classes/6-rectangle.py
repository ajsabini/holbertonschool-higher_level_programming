#!/usr/bin/python3
"""classes"""


class Rectangle:
    """define the rectangle class"""
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """calculate area"""
        return self.__width * self.__height

    def perimeter(self):
        """calculate perimeter"""
        return (self.__width + self.__height) * 2

    def __str__(self):
        """String representation"""
        res = ""
        if self.__width * self.__height == 0:
            return res
        else:
            for i in range(self.__height):
                res += "#" * self.__width + '\n'
            return res[:-1]

    def __repr__(self):
        """Representation"""
        res = "Rectangle (" + str(self.__width) + ", " + str(self.__height) + ")"
        return res

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
