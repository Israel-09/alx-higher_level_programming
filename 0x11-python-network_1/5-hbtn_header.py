#!/usr/bin/python3
'''displays the response from a web server
'''
import requests
import sys

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    r_id = r.headers.get('X-Request-Id')
    print('{}'.format(r_id))
