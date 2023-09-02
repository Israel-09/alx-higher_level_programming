#!/usr/bin/python3
'''post a request to a web server
'''

if __name__ == '__main__':
    import sys
    import requests

    headers = {'Accept': 'application/vnd.github+json',
               'X-GitHub-Api-Version': '2022-11-28'
               }
    url = 'https://api.github.com/repos/{}/{}/commits'.\
          format(sys.argv[2], sys.argv[1])
    response = requests.get(url, headers=headers)

    try:
        json_arr = response.json()
        if len(json_arr) == 0:
            print('No result')
        else:
            count = 0
            for json_obj in json_arr:
                url = json_obj.get('author').get('url')
                user = requests.get(url, headers=headers)
                name = user.json().get('name')
                if count < 10:
                    print('{}: {}'.format(json_obj.get('sha'), name))
                else:
                    break
                count += 1
    except simplejson.errors.JSONDecodeError:
        print('Not a valid JSON')
