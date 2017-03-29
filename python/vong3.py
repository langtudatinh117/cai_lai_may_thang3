# coding=utf-8
import requests
from pymongo import MongoClient
import json

s = requests.Session()
s.headers = {'user-agent': 'Chrome/56.0.2924.87'}

URL_G_METHOD = 'http://123.30.174.146:8056/assd?method='
##################################
client = MongoClient("ds023408.mlab.com", 23408)
db = client['anhsang']
db.authenticate('daoan', '0903293343')
collection = db['vong1_2']


def getQues(token):
    ques = s.get(URL_G_METHOD + 'get_ques&token=' + token)
    return json.loads(ques.content)['data']['ques']


def getAns(q):
    doc = collection.find_one({'ques': q})
    if doc is not None:
        return doc['ans']

while True:
    print (getAns(getQues("NA1OCAxmioZXAA-QBn19R0fCk9HUeETf")))
    a = raw_input()