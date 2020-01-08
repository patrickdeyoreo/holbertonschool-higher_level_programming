#!/bin/bash
#
# Send a GET request to a URL and display the body of the response
# Usage: 1-body.sh URL

curl -sL -- "$1"
