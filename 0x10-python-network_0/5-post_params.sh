#!/usr/bin/env bash
#a Bash script that takes in a URL as an argument, sends a POST
# request to the URL.

var1="email=test@gmail.com"
var2="subject=I will always be here for PLD"

curl -X POST -d "$var1&$var2" "$1";
