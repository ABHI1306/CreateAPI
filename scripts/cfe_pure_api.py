import requests

BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = "api/updates/"

def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    status_code = r.status_code
    if status_code != 200:
        print('probably not good sign?')
    data = r.json()

    for obj in data:
        if(obj['id'] == 1):
            r2 = requests.get(BASE_URL + ENDPOINT + str(obj['id']))
            print(r2.json())
    return data

print(get_list())