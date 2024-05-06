#!/usr/bin/env bash
#This is to bring out accepted HTTP request by a server

#  $1 => URL to test
# Send an OPTIONS request to the server and capture the allowed methods
allowed_methods=$(curl -sI -X OPTIONS -I "$1" | grep -i "^Allow:" | cut -d " " -f 2-)

# Display the allowed methods
echo "$allowed_methods"
