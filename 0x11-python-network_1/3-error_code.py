#!/usr/bin/python3
'''sends a request to the URL and displays the
value of the X-Request-Id'''
import urllib.request
import sys

if __name__ == '__main__':

    req = urllib.request.Request(sys.argv[1])
    try:
        page = urllib.request.urlopen(req).read()
        print('{}'.format(page.decode('utf-8')))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
