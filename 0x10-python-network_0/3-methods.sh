#!/usr/bin/env bash
#p
curl -sI $1 | grep Allow | cut -c 8-
