import requests
import json
def get_data(id =None):
    URL = "http://127.0.0.1:8000/info/"+str(id)
    data={}
    if id is not None:
        data={"id":id}
    json_data=json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    r = requests.get(url=URL,headers=headers,data=json_data)
    json_data = r.json()
    print(json_data)
#get_data(5)
def post():
    URL = "http://127.0.0.1:8000/info/"
    data ={

        'ename' : "youth",
        'eno' : 11,
        "esal" : 10000,
        "eaddr" : "hyd"
    }
    headers={'Content-Type' : 'application/json'}
    json_data=json.dumps(data)
    r = requests.post(url=URL , headers=headers ,data=json_data)
    data=r.json()
    print(data)
#post()
def update(id=None):
    URL = "http://127.0.0.1:8000/info/"+str(id)+'/'
    data ={
     #   'id': 3,
        "ename" : 'durgaaaaa',
        'eno' : 1100000,
        'esal':1234,
        'eaddr' : 'dubai'
    }
    json_data=json.dumps(data)
    headers = {'Content-Type': 'application/json'}
    r = requests.put(url=URL , headers=headers,data=json_data)
    data=r.json()
    print(data)
#update(3)
def delete():
    URL = "http://127.0.0.1:8000/info/"
    data ={'id': 7}
    json_data=json.dumps(data)
    r = requests.delete(url=URL , data=json_data)
    data=r.json()
    print(data)
#delete()