#!/bin/bash
# displays the methods allowed
curl -sI "$1" | grep 'Allow' | cut -c 8-
