#!/bin/bash
#MINE
#curl -so /dev/null "$1" -w "%{size_download}" OR
curl -sI $1 | grep -i  -e Content-Length | cut -d ' ' -f 2
