#!/usr/bin/python3
"""module - class student"""


class Student:
    """class student"""
    def __init__(self, first_name, last_name, age):
        """init the obj th class, fn, ln, age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """function that return a dict of a Student instance"""
        return self.__dict__
