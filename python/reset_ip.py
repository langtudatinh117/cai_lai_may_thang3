import requests
import re
import timeit

cookies = {'Authorization': 'Basic YWRtaW4gIURhb2FuNzkxMTM3'}


def getIp():
    return requests.get('https://api.ipify.org/').text


def getView():
    url = 'http://192.168.1.1/wancfg.cmd?action=view'
    return requests.get(url, cookies=cookies).text


def getKey(req):
    pattern = r"sessionKey=\d+"
    c = re.compile(pattern)
    return c.findall(req)[-1]


def disconnect(key):
    url = 'http://192.168.1.1/wancfg.cmd?action=manual&manual=0&ifname=ppp0.4&' + key
    return requests.get(url, cookies=cookies).text


def connect(key):
    url = 'http://192.168.1.1/wancfg.cmd?action=manual&manual=1&ifname=ppp0.4&' + key
    return requests.get(url, cookies=cookies).text

def reset():
    connect(getKey(disconnect(getKey(getView()))))
