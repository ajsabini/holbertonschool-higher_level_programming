#!/bin/bash
# 
curl -s "$1" | grep 'Content-Length' | awk '{print $2}'
