#!/bin/bash
#MINE
#curl -sw "%{size_download}\n" $1 --> This doesnt work perfectly 
curl -sI $1 | grep -e Content-Length | cut -d ' ' -f 2
