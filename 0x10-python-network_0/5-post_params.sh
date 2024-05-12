#!/bin/bash
# This is a comment
curl  POST -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD"  "$1" # 1>/dev/null
