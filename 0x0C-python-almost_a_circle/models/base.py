#!/usr/bin/python3
"""module - base"""
import json


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
            with open(ls.__name__ + ".json", "w") as f:
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
        new_obj = cls(2, 4)
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        my_dict = {}
        my_list = []
        try:
            with open(cls.__name__ + ".json", "r") as f:
                my_dict = json.load(f)
        except Exception:
            return my_list
        for dictio in my_dict:
            my_list.append(cls.create(**dictio))
        return my_list
