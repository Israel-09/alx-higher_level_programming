#!/usr/bin/python3
'''sends a request to the URL and displays
the body of the response'''

if __name__ == '__main__':
    import sys
    import urllib.request
    try:
        req = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8')
            print('{}'.format(body))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
