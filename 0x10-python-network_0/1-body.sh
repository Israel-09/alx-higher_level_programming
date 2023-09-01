#!/usr/bin/env bash
# a Bash the displays the content of the body of the response of a url

response=$(curl -sL -w "%{http_code}" -o /dev/null "$1";)

if (( response == 200 )); then
	curl -s "$1"
fi
