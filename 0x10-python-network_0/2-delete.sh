#!/bin/bash
# sends a DELETE request to the URL passed as first argument
curl -s "$1" -X DELETE
