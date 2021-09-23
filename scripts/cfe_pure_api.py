import requests
import json

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

def create_update():
    new_data = {
        'user': 1,
        'content': "Another more cool content" 
    }
    r = requests.post(BASE_URL + ENDPOINT,data=json.dumps(new_data))
    print(r.headers)
    print(r.status_code)
    if(r.status_code == requests.codes.ok):
        return r.json()
    return r.text

print(create_update())
#print(get_list())

def do_obj_update():
    new_data = {
        'content': "New obj data" 
    }
    r = requests.put(BASE_URL + ENDPOINT + "1" + "/",data=json.dumps(new_data))
    print(r.headers)
    print(r.status_code)
    if(r.status_code == requests.codes.ok):
        return r.json()
    return r.text

def do_obj_delete():
    new_data = {
        'content': "New obj data" 
    }
    r = requests.delete(BASE_URL + ENDPOINT + "1" + "/")
    print(r.headers)
    print(r.status_code)
    if(r.status_code == requests.codes.ok):
        return r.json()
    return r.text

#print(do_obj_update())
