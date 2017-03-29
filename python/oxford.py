from __future__ import print_function
from pymongo import MongoClient
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

################################
client = MongoClient("ds137759.mlab.com", 37759)
db = client['huplib']
db.authenticate('daoan', '0903293343')
oxford = db['oxford']
pending = db['pending']

###############
query = 'concern_1'
URL = 'http://www.oxfordlearnersdictionaries.com/definition/english/' + query


def getSoup(url):
    try:
        html = urlopen(url)
    except:
        return None
    return html.read()


def getLink(soup):
    try:
        p = re.compile("^(http:\/\/www.oxfordlearnersdictionaries.com\/definition\/english\/)((?!#).)*$")
        li = p.findall(soup)
    except:
        return None
    return li


def linkToQuery(link):
    _query = [e.split('/')[-1] for e in link]
    return list(set(_query))


def getWord(soup):
    print(soup)
    p = re.compile("<h2 class=\"h\">(.*)</h2>")
    return p.findall(soup)


while True:
    Soup = getSoup(URL)
    Word = getWord(Soup)
    lst_query = linkToQuery(getLink(Soup))

    pending.update({'query': query}, {'$set': {'status': 'ok'}})
    lst_query.remove(query)

    for q in lst_query:
        doc = pending.find_one({'query': q})
        if doc is None:
            pending.insert_one({'query': q, 'status': 'pending'})

    document = oxford.find_one({'word': Word})
    if document is None:
        oxford.insert_one({'word': Word, 'query': [query]})
    elif query not in document['query']:
        one_set = set(document['query'])
        one_set.add(query)
        oxford.update({'word': Word}, {'$set': {'query': list(one_set)}})

    doc_q = pending.find_one({'status': 'pending'})
    if doc_q is not None:
        query = doc_q['query']
        URL = 'http://www.oxfordlearnersdictionaries.com/definition/english/' + query
    else:
        break
