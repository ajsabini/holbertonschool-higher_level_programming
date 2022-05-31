#!/usr/bin/python3
""""""


import json
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


try:
    obj = load_from_json_file('add_item.json')
    save_to_json_file(obj + argv[1:], 'add_item.json')
except Exception as e:
    save_to_json_file(argv[1:], 'add_item.json')
