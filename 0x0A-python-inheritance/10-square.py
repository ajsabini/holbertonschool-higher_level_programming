#!/usr/bin/python3
"""module - create a square"""

base = __import__('9-rectangle').Rectangle


class Square(base):
    """Square class"""

    def __init__(self, size):
        """def sqaure class"""
        self.integer_validator("size", size)
        super().__init__(size, size)
