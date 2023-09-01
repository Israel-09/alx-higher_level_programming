#!/usr/bin/python3
'''post a request to a web server
'''

if __name__ == '__main__':
    import sys
    import requests
    
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error: {}".format(response.status_code))
    else:
        response.encoding = 'utf-8'
        print('{}'.format(response.text))
