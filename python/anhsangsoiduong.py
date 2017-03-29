# coding=utf-8
import random
import string
from bs4 import BeautifulSoup
import requests
import re
from pymongo import MongoClient
import json
from collections import Counter
import ast

s = requests.Session()
s.headers = {'user-agent': 'Chrome/56.0.2924.87'}
URL_REG = 'http://anhsangsoiduong.vn/register.html'
URL_INFO = 'http://anhsangsoiduong.vn/user/user/update-profile-assd'
URL_GAME = 'http://anhsangsoiduong.vn/assd/exam/play-exam'
URL_G_METHOD = 'http://123.30.174.146:8056/assd?method='

########################################
#
client = MongoClient("ds023408.mlab.com", 23408)
db = client['anhsang']
db.authenticate('daoan', '0903293343')
collection = db['vong1_2']
vong3 = db['vong3_2']


def id_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def getToken(res):
    bsObj = BeautifulSoup(res.content, 'lxml')
    token = bsObj.find(attrs={"name": "_csrf"}).attrs['value']
    return token


def regAcc():
    user_and_pass = id_generator(8)
    res = s.get(URL_REG)
    token = getToken(res)
    body = {"_csrf": token, "RegisterForm[username]": user_and_pass, "RegisterForm[password]": user_and_pass,
            "RegisterForm[passwordReType]": user_and_pass, "RegisterForm[phone]": ""}
    r = s.post(URL_REG, data=body)
    if r.status_code == 200:
        return user_and_pass


def updateInfo():
    hoten = 'Dan tri'
    gioitinh = 'male'
    ngaysinh = "-".join(
        str(e) for e in [random.randrange(1994, 1999, 1), random.randrange(1, 12, 1), random.randrange(1, 28, 1)])
    cmt = ''.join(random.choice(string.digits) for _ in range(10))
    phone = '09' + ''.join(random.choice(string.digits) for _ in range(8))
    email = id_generator(8) + '@gmail.com'
    city = '7'
    school_id = '31634'
    ma_sv = ''.join(random.choice(string.digits) for _ in range(6))
    khoa = ma_sv
    lop = ma_sv
    token = getToken(s.get(URL_INFO))
    body = {"_csrf": token, "UpdateInfoFormASSD[full_name]": hoten, "UpdateInfoFormASSD[gender]": gioitinh,
            "UpdateInfoFormASSD[birthday]": ngaysinh,
            "UpdateInfoFormASSD[cmt]": cmt, "UpdateInfoFormASSD[phone]": phone,
            "UpdateInfoFormASSD[email]": email, "UpdateInfoFormASSD[city_id]": city,
            "UpdateInfoFormASSD[school_id]": school_id, "UpdateInfoFormASSD[ma_sv]": ma_sv,
            "UpdateInfoFormASSD[khoa]": school_id, "UpdateInfoFormASSD[lop]": ma_sv}
    res = s.post(URL_INFO, data=body)
    return res.status_code


def getTokenGame():
    res = s.get(URL_GAME)
    bsObj = BeautifulSoup(res.content, 'lxml')
    token = bsObj.find('iframe').attrs['src']
    p = re.compile("token=(.*)&link")
    return "".join(p.findall(token))


def startGame(token):
    s.get(URL_G_METHOD + 'start&token=' + token + '&type=2')


def getQues(token):
    ques = s.get(URL_G_METHOD + 'get_ques&token=' + token)
    ans = json.loads(ques.content)['data']['ans']
    data = {"ques": json.loads(ques.content)['data']['ques'], "ans": [ans[0], ans[1], ans[2], ans[3]]}
    return data


def getAns(token):
    ans = s.get(URL_G_METHOD + 'ans_ques&token=' + token + '&ans=0')
    return json.loads(ans.content)['data']


def getQAndA(token):
    Quiz = getQues(token)
    Quiz['ans'] = Quiz['ans'][int(getAns(token)['ans'])]
    return Quiz


def savaDB(q):
    doc = collection.find_one({'ques': q['ques']})
    if doc is None:
        collection.insert_one(q)


def continueGame(token):
    s.get(URL_G_METHOD + 'continue&token=' + token)


print (regAcc())
updateInfo()
# while True:
#     regAcc()
#     updateInfo()
#     TOKEN = getTokenGame()
#     print TOKEN
#     startGame(TOKEN)
#     for num in range(0, 20):
#         try:
#             quiz = getQAndA(TOKEN)
#             savaDB(quiz)
#         except:
#             continue

#     continueGame(TOKEN)
#     for num1 in range(0, 20):
#         try:
#             quiz = getQAndA(TOKEN)
#             savaDB(quiz)
#         except:
#             continue

#     continueGame(TOKEN)
#     ques = s.get(URL_G_METHOD + 'get_ques&token=' + TOKEN)
#     try:
#         aList = json.loads(ques.content)['data']['a']
#         bList = json.loads(ques.content)['data']['b']
#         for item in aList:
#             doc = vong3.find_one({"a": item})
#             if doc is None:
#                 vong3.insert_one({"a": item, "b": str(dict(Counter(bList)))})
#             else:
#                 bTrongDB = ast.literal_eval(doc['b'])
#                 for bItem in bList:
#                     if bItem in bTrongDB:
#                         bTrongDB[bItem] = int(bTrongDB[bItem]) + 1
#                 vong3.update({"a": item}, {'$set': {'b': str(bTrongDB)}})
#     except:
#         print ("loi")
#     finally:
#         s = requests.Session()
#         s.headers = {'user-agent': 'Chrome/56.0.2924.87'}
