#!/usr/bin/python3
""" takes in a url, sends request to the url -
and displays value of X-Request-ID in response header
"""


import requests
import sys

if __name__ == "__main__":
	req = requests.get(sys.argv[1])
	print(req.headers.get('X-Request-ID'))
