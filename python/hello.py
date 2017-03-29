import urllib3
from bs4 import BeautifulSoup
import re

http = urllib3.PoolManager()


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


####header####

def getHeader(source):
    try:
        return source.find('div', class_="di-head normal-entry")
    except:
        return None


def getWord(source):
    try:
        return source.find('h2', class_="di-title cdo-section-title-hw").get_text()
    except:
        return None


def getOriginalWord(source):
    try:
        return source.find('span', class_="hw").get_text()
    except:
        return None


def getPartOfSpeech(source):
    try:
        return source.find('span', class_="pos").get_text()
    except:
        return None


def getGram(source):
    try:
        return source.find('span', class_="gram").get_text()
    except:
        return None


def getSpeechUK(source):
    try:
        return source.find('span', class_="circle circle-btn sound audio_play_button uk").attrs['data-src-ogg']
    except:
        return None


def getSpeechUS(source):
    try:
        return source.find('span', class_="circle circle-btn sound audio_play_button us").attrs['data-src-ogg']
    except:
        return None


def getSpellvar(source):
    try:
        return source.find('span', class_="spellvar")
    except:
        return None


def getIpa(source):
    try:
        return source.find('span', class_="ipa").get_text()
    except:
        return None


def getInf(source):
    try:
        lst = []
        for e in source.findAll('span', class_="inf"):
            lst.append(e.get_text().strip())
    except:
        return None
    else:
        if len(lst) == 0:
            return None
        else:
            return lst


def getLab(source):
    try:
        lst = []
        for e in source.findAll('span', class_="lab"):
            lst.append(e.get_text().strip())
    except:
        return None
    else:
        if len(lst) == 0:
            return None
        else:
            return lst


def getVar(source):
    try:
        lst = []
        for e in source.findAll('span', class_="v"):
            lst.append(e.get_text().strip())
    except:
        return None
    else:
        if len(lst) == 0:
            return None
        else:
            return lst


####END header####

source_body = getSource('http://dictionary.cambridge.org/dictionary/learner-english/a_1')

header = getHeader(source_body)

print(getWord(header))
print(getPartOfSpeech(header))
print(getGram(header))
print(getIpa(header))
print(getSpeechUK(header))
print(getSpeechUS(header))
print(getLab(header))
print(getInf(header))
print(getVar(header))

if getPartOfSpeech(header) == 'phrasal verb':
    print(getOriginalWord(header))
