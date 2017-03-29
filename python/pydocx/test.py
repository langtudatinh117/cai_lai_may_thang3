# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import r

title = "Kim HJ, Bae SC Histone deacetylase inhibitors: molecular mechanisms of +\
action and clinical trials as anti-cancer drugs"


def get_link_ref(q):
    res = requests.get('https://scholar.google.com.vn/scholar?q=' + q)
    bsObj = BeautifulSoup(res.content, 'lxml')
    line_ref = bsObj.find('div', class_="gs_ri").find(
        'a', attrs={"role": "button"})['onclick']
        id_ref = re.search(r"event\,\'(.*)\'\,\'",
                           line_ref).group(1)
        res2 = requests.get(
            "https://scholar.google.com.vn/scholar?q=info:" +
            + id_ref +
            + ":scholar.google.com/&output=cite&scirp=0&hl=vi")
    bsObj2 = BeautifulSoup(res2.content, 'lxml')
    return bsObj2.find('a')['href']


print get_link_ref(title)
