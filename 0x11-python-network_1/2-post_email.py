#!/usr/bin/python3
""" takes in a url and email sends a post
	request to the passed url w email as
	parameter and display body response
"""


from sys import argv
import urllib.request
import urllib.parse

if __name__ == "__main__":

    mail = {'email': argv[2]}
    data = parse.urlencode(mail)
    req = request.Request(argv[1], mail)
    with request.urlopen(req, data) as response:
        html = response.read()
        print(html.decode('utf-8'))
