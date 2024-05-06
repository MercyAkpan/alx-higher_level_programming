#!/bin/bash
# This add a temporary header to a HTTPS request and prints out body of response
curl -sH "X-School-User-Id: 98" "$1"
# var='X-meme-Id: 98'
# NOTE: delimitter is a colon.
# To view the header just added
#curl -viH "$var" www.mercyakpan.tech 2>&1 | grep -i "$var" | awk -F': ' '{print substr($0, 3)}'
