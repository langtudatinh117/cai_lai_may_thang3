import urllib3
from bs4 import BeautifulSoup
import re

http = urllib3.PoolManager()
URL = 'http://dictionary.cambridge.org/dictionary/learner-english/mound'
_class = ''
lst1 = []


def getSource(url):
    try:
        r = http.request('GET', url)
    except:
        return None
    try:
        bsObj = BeautifulSoup(r.data, 'lxml')
        source = bsObj.body
    except:
        return None
    return source


def getHeader(source):
    try:
        return source.find('span', class_="di-info")
    except:
        return None


def getNextLink(source):
    try:
        lst = source.find('ul', class_="unstyled a--b a--rev a--alt")
        return [a.attrs['href'] for a in lst.findAll('a', href=True)][4]
    except:
        return None


while True:
    source_body = getSource(URL)
    header = getHeader(source_body)
    try:
        _class = [e.attrs['class'] for e in header.findAll("span")]
        _class = [item for sublist in _class for item in sublist]
        lst1 = list(set(list(set(_class)) + lst1))
    except:
        print("idiom")
    else:
        print(URL + "\n" + str(lst1))
    finally:
        URL = getNextLink(source_body)
