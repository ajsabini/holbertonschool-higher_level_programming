#!/usr/bin/python3
""" takes in a url and an email, sends a POST req
to the passed url w email as a parameter, and
finally display body response -
"""


import requests
import sys

if __name__ == "__main__":

	req = requests.post(sys.argv[1], data={'email': sys.argv[2]})
	print(req.text)
