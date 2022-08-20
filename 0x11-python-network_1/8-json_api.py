#!/usr/bin/python3
""" takes in a letter and sends a POST request
to an url w the letter as a parameter
"""


import requests
from sys import argv

if __name__ == "__main__":
	req = requests.get(argv[1])
	if req.status_code > 399:
		print("Error code: {}".format(req.status_code))
	else:
		print(req.text)
