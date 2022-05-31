#!/usr/bin/python3
"""module - base geometry"""


class BaseGeometry:
    """class base geometry"""

    def area(self):
        """building instance"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """int validation"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
