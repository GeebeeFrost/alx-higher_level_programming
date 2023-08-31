#!/bin/bash
# sends a GET request to a URL along with a header variable
curl -sH "X-School-User-Id: 98" "$1"
