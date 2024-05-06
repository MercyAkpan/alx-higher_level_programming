#!/bin/bash
# This add a temporary header to a HTTPS request and prints out body of response
curl -sH "X-School-User-Id: 98" "$1"
