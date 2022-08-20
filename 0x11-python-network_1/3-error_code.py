#!/usr/bin/python3
""" takes in a url, sends a req to the url and
displays body response, decode utf-8 """


import urllib.request
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
	try:
		with urllib.request.urlopen(argv[1]) as response:
			print(response.read().deode("utf-8", "replace"))
	except HTTPError as e:
		print("Error code: {}".fomrat(e.code))
