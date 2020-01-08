#!/bin/bash
#
# Send a GET request to a URL and display the body of the response
# The header parameter X-HolbertonSchool-User-Id will be sent with the value 98
# Usage: 4-header.sh URL

curl -sL -H 'X-HolbertonSchool-User-Id: 98' -- "$1"
