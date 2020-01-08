#!/bin/bash
#
# Send a request to that URL and display the size of the body of the response
# Usage: 0-body_size.sh URL

curl -sLI -- "$1" | grep -i 'content-length' | tr -s '\t ' ' ' | cut -d ' ' -f 2
