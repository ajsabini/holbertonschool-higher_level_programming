#!/usr/bin/python3
"""create a class"""


class Square:
    """the class Square, that defines a square"""
    def __init__(self, size=0):
        """instantiation"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """public method"""
        return self.__size ** 2

    @property
    def size(self):
        """recover size(private) information"""
        return self.__size

    @size.setter
    def size(self, value):
        """set the value"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """my_print - is a method, printin the square in the stdout"""
        if self.__size > 0:
            for x in range(self.__size):
                for y in range(self.__size):
                    print('#', end="")
                print("")
        else:
            print("")
