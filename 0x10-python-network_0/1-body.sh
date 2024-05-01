#!/bin/bash
#MINE
status_code=$(curl -s -w "%{http_code}" "$1" -o  /dev/null) && [ "$status_code" == "200" ] && curl -s "$1"
