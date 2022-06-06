#!/usr/bin/python3
"""module - rectangle"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """building object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter __width"""
        return self.__width

    @width.setter
    def width(self, width):
        """ setter __width """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """getter __height"""
        return self.__height

    @height.setter
    def height(self, height):
        """setter __height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """getter __x"""
        return self.__x

    @x.setter
    def x(self, x):
        """setter __x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """getter __y"""
        return self.__y

    @y.setter
    def y(self, y):
        """setter __y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """calculate rectangle area"""
        return self.__height * self.__width

    def display(self):
        """print in stdout the rect inst with #"""
        for i in range(self.__y):
            print("\n", end="")
        for x in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """override __str__ method"""
        str1 = "[Rectangle] ({self.id}) {self.__x}"
        str2 = "/{self.__y} - {self.__width}/{self.__height}"
        return f{str1} + {str2}

    def update(self, *args, **kwargs):
        """assign arguments to atrtiues"""
        atribs = {0: "id", 1: "width", 2: "height", 3: "x", 4: "y"}
        if args and args is not None:
            if len(args) <= 5:
                for n in range(len(args)):
                    setattr(self, atribs[n], args[n])
        else:
            for m in kwargs:
                setattr(self, m, kwargs[m])

    def to_dictionary(self):
        """return dictionary representation"""
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
