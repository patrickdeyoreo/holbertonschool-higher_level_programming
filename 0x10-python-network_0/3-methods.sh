#!/bin/bash
#
# Display all HTTP methods the server of a URL will accept
# Usage: 3-methods.sh URL

curl -sLI -- "$1" | grep -i 'allow' | tr -s '\t ' ' ' | cut -d ' ' -f 2
