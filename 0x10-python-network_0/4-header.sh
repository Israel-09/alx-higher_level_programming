#!/bin/bash
#a Bash script that takes in a URL as an argument, sends a GET
curl -s -H 'X-school-user-id:98' "$1";
