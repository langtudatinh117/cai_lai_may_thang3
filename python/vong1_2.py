# coding=utf-8
import requests
from pymongo import MongoClient
import json
import ast

s = requests.Session()
s.headers = {'user-agent': 'Chrome/56.0.2924.87'}
TOKEN = ""
URL_G_METHOD = 'http://123.30.174.146:8056/assd?method='
##################################
client = MongoClient("ds023408.mlab.com", 23408)
db = client['anhsang']
db.authenticate('daoan', '0903293343')
collection = db['vong1_2']
vong3 = db['vong3_2']


def getQues(token):
    ques = s.get(URL_G_METHOD + 'get_ques&token=' + token)
    return json.loads(ques.content)['data']['ques']


def getAns(q):
    doc = collection.find_one({'ques': q})
    if doc is not None:
        return doc['ans']


def round3(token):
    ques = s.get(URL_G_METHOD + 'get_ques&token=' + token)
    aList = json.loads(ques.content)['data']['a']
    bList = json.loads(ques.content)['data']['b']
    for item in aList:
        doc = vong3.find_one({"a": item})
        if doc is not None:
            bTrongDB = ast.literal_eval(doc['b'])
            result = list(filter(lambda x: bTrongDB[x] == max(bTrongDB.values()), bTrongDB))
            print ('----' + item)
            for item_b in bList:
                if item_b in result:
                    print (item_b)


while True:
    TOKEN = raw_input()
    for i in range(0, 40):
        print (getAns(getQues(TOKEN)))
        a = raw_input()
    round3(TOKEN)
    break
