#!/usr/bin/python3
"""create a class"""


class Square:
    """the class Square, that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """instantiation"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
            self.__position = position

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

    @property
    def position(self):
        """recover position(priv) information"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the new value of position"""
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """my_print - is a method, printin the square in the stdout"""
        if self.__size == 0:
            print()
        else:
            position = self.__position
            if position[1] > 0:
                for i in range(position[1]):
                    print()
            for y in range(self.size):
                print(" " * position[0] + "#" * self.size)
