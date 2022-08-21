#!/usr/bin/python3
""" takes in a url and email sends a post
	request to the passed url w email as
	parameter and display body response
"""


from sys import argv
from urllib import request
from urllib import parse

if __name__ == "__main__":
	
    mail = {'email': argv[2]}
    data = parse.urlencode(mail)
    data = data.encode()
    url = argv[1]
    with request.urlopen(url, data) as response:
        html = response.read()
        print(html.decode('utf-8'))
