#!/usr/bin/env bash
# comment
allowed_methods=$(curl -sI -X OPTIONS -I "$1" | grep -i "^Allow:" | cut -d " " -f 2-) && echo "$allowed_methods"
