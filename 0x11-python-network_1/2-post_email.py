#!/usr/bin/python3
"""  """


from sys import argv
import urllib.request
import urllib.parse

if __name__ == "__main__":
	mail = {'email': argv[2]}
	data = urllib.parse.urlencode(mail)
	req = urllib.request.Request(argv[1], mail)
	with urllib.request.urlopen(req) as response:
		html = response.read()
		print(html.decode('utf-8'))
