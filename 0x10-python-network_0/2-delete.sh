#!/bin/bash
#
# Send a DELETE request to a URL and display the body of the response
# Usage: 2-delete.sh URL

curl -sL -X DELETE -- "$1"
