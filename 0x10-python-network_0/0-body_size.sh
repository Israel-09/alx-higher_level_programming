#!/bin/bash
# a Bash the displays the size of the body of the response of a url
curl -sI "$1" | grep 'Content Length' | cut -d ' ' -f 2
