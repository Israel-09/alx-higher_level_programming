#!/usr/bin/python3
'''displays the response from a web server
'''
import urllib.request

if __name__ == '__main__':
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print('Body response:')
        print('    - type: {}'.format(type(page)))
        print('    - content: {}'.format(page))
        print('    - utf8 content: {}'.format(page.decode('utf-8')))
