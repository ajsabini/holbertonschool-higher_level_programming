#!/usr/bin/python3
"""module - Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """building object"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getting size"""
        return self.height

    @size.setter
    def size(self, size):
        """setting size"""
        self.width = size
        self.height = size

    def __str__(self):
        """override __str__"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """assign arg to atributes"""
        atribs = {0: "id", 1: "size", 2: "x", 3: "y"}
        if args and args is not None:
            if len(args) <= 4:
                for n in range(len(args)):
                    setattr(self, atribs[n], args[n])
        else:
            for m in kwargs:
                setattr(self, m, kwargs[m])

    def to_dictionary(self):
        """returns dictionary representation of a square"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
