#!/bin/bash
#
# Send a POST request to a URL and display the body of the response
# Usage: 5-post_params.sh URL

curl -sL -d 'email=hr@holbertonschool.com' -d 'subject=I will always be here for PLD' -- "$1"
