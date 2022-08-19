#!/bin/bash
# takes in a URL and displaus all HTTP methods allow
curl -sI "$1" | grep "Allow:" | cut -d' ' -f 2-
