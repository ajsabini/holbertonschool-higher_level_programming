#!/usr/bin/python3
"""module - base"""
import json
from os import path


class Base:
    """class - Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """building object"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON string repr of a list dictionary"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write JSON string representation of list obj to a file"""
        obj_list = []
        if list_objs is None:
            with open(cls.__name__ + ".json", "w") as f:
                f.write(cls.to_json_string(obj_list))
        else:
            for obj in list_objs:
                obj_list.append(cls.to_dictionary(obj))
            with open(cls.__name__ + ".json", 'w') as f:
                f.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """return json strin to dictionary obj"""
        obj_list = []
        if json_string is None:
            return obj_list
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance w/atribs already set"""
        if cls.__name__ == "Rectangle":
            new_obj = cls(2, 4)
        if cls.__name__ == "Square":
            new_obj = cls(2)
        if new_obj:
            new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        fn = cls.__name__ + '.json'
        if path.isfile(fn):
            with open(fn, 'r', encoding='utf-8') as f:
                dict = cls.from_json_string(f.read())
            return [cls.create(**obj) for obj in dict]
        return []
