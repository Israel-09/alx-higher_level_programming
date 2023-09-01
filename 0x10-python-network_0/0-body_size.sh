#!/usr/bin/env/ bash
# a Bash the displays the size of the body of the response of a url

curl -I $1 | grep 'Content Length' | cut -d ' ' -f 2
