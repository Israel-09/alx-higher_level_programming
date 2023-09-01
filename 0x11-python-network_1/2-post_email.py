#!/usr/bin/python3
'''sends a request to the URL and displays the
value of the X-Request-Id'''
import urllib.request
import sys

if __name__ == '__main__':
    
    data = sys.argv[2].encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print('{}'.format(page.decode('utf-8')))
