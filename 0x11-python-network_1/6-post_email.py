#!/usr/bin/python3
'''post a request to a web server
'''

if __name__ == '__main__':
    import sys
    import requests

    email = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], data=email)
    response.encoding = 'utf-8'
    print('{}'.format(response.text))
