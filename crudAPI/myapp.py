import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data = {}
    if id is not None :
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL,data= json_data)
    
    data = r.json()
    print(data)
     
def post_data():
    data = {
        'name' : 'kdbhai',
        'roll' : 101,
        'city' : 'surat',
    }   
    
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)
    
def update_data():
    data = {
        'id' : 4,
        'name' : 'yoyo',
        'roll' : 34,
        'city' : 'efn',
    }   
    
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)
    
def partial_update_data():
    data = {
        'id' : 4,
        'name' : 'yoy0o',
        'roll' : 34,   
    }   
    
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)
    
def delete_data():
    data = {'id' : 8 }   
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)
    
    
# get_data(6)
# post_data()
# update_data()
# partial_update_data()
delete_data()
    