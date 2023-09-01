#!/bin/bash
#a Bash script that takes in a URL as an argument, sends a POST request to the URL.
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1";
