#!/usr/bin/python3
""" takes in a url, sends a request to the url an display x-request-id """


from sys import argv
import urllib.request

if __name__ == "__main__":

    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
