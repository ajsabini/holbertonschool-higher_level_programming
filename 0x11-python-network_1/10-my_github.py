#!/usr/bin/python3
"""scripot takes your github credentials, and use GH api"""


from requests import get
from sys import argv

if __name__ == "__main__":

    req = get("https://api.gitub.com/user",
              auth=(argv[1], argv[2])).json()

    try:
        print(req["id"])
    except Exception:
        print(None)
