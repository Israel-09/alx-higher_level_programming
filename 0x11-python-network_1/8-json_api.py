#!/usr/bin/python3
'''post a request to a web server
'''

if __name__ == '__main__':
    import sys
    import requests

    value = ''
    if len(sys.argv) > 1:
        value = sys.argv[1]
    request_dict = {'q': value}
    response = requests.post("http://0.0.0.0:5000/search_user",
                             data=request_dict)

    try:
        json_obj = response.json()
        if len(json_obj) == 0:
            print('No result')
        else:
            print('[{}] {}'.format(json_obj.get('id'),
                                   json_obj.get('name')))
    except simplejson.errors.JSONDecodeError:
        print('Not a valid JSON')
