#!/bin/bash
# takes an urll as an arg, sends a GET request to the URL, and displays the body
curl -s "$1" -H "X-HolbertonSchool-User-Id: 98"
