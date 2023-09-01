#!/usr/bin/python3
'''post a request to a web server
'''

if __name__ == '__main__':
    import sys
    import requests

    headers = {'Accept': 'application/vnd.github+json',
               'Authorization': 'Bearer {}'.format(sys.argv[2]),
               'X-GitHub-Api-Version': '2022-11-28'
               }
    url = 'https://api.github.com/users/{}'.format(sys.argv[1])
    response = requests.get(url, headers=headers)

    try:
        json_obj = response.json()
        if len(json_obj) == 0:
            print('No result')
        else:
            print('{}'.format(json_obj.get('id')))
    except simplejson.errors.JSONDecodeError:
        print('Not a valid JSON')
