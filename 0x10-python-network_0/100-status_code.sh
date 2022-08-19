#!/bin/bash
# send a request to a URL passed as an arg, and display status code
curl -sI -w '%{response_code}' "$1" -o /dev/null
