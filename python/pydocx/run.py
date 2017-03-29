# -*- coding: utf-8 -*-
import re
import scholarly
import requests
import bibtexparser
from bs4 import BeautifulSoup
import PyICU


collator = PyICU.Collator.createInstance(PyICU.Locale('pl_PL.UTF-8'))


def get_order_and_title():
    file_ref = open('an2.txt', 'r')
    obj_ref = file_ref.readlines()
    result = {}
    for idx, line in enumerate(obj_ref):
        m = re.findall("\(\d{4}\)\. (.+)\. ", line)
        if m != []:
            result.update({idx + 1: m[0]})
        else:
            result.update({idx + 1: ''})
    file_ref.close()
    return result


def get_data_ref(query):
    search_query = scholarly.search_pubs_query(query)
    bibtext = requests.get(next(search_query).url_scholarbib)
    bib_database = bibtexparser.loads(bibtext.content)
    return bib_database.entries[0]


def get_author(title):
    return get_data_ref(title)['author']


def refactor_author(authors):
    lst_author = authors.split(' and ')
    result = ''
    for idx, author in enumerate(lst_author):
        if author == 'others':
            break
        if idx == 3:
            result += 'et al '
            break
        family = author.split(',')[0]
        given = ''.join([i for i in author.split(',')[1] if i.isupper()])
        r_author = family + ' ' + given
        result += r_author + ', '
    return result


def get_author_pm_by_title(title):
    q = 'https://www.ncbi.nlm.nih.gov/pubmed/?term=' + title + '[Title]'
    q = q.replace('and', '[Title] and')
    q = q.replace('–', '-')
    res = requests.get(q)
    result = ''
    bsObj = BeautifulSoup(res.content, 'lxml')
    try:
        authors = bsObj.find(attrs={"class": "auths"}).find_all('a')
    except:
        titles = bsObj.find_all(attrs={"class": "title"})
        for t in titles:
            isMatch = re.match(title, t.get_text())
            if (isMatch):
                res = requests.get(
                    'https://www.ncbi.nlm.nih.gov' + t.find('a')['href'])
                bsObj = BeautifulSoup(res.content, 'lxml')
                authors = bsObj.find(attrs={"class": "auths"}).find_all('a')
                break
    finally:

        lst_authors = [author.get_text() for author in authors]
        if len(lst_authors) > 3:
            for i in range(3):
                result += lst_authors[i] + ', '
            result += 'et al '
        else:
            for idx, author in enumerate(lst_authors):
                if idx == len(lst_authors) - 1:
                    result += author + " "
                else:
                    result += author + ', '
        return result


def get_author_pm_by_doi(doi):
    result = ''
    q = 'https://www.ncbi.nlm.nih.gov/pubmed/?term=' + doi
    res = requests.get(q)
    bsObj = BeautifulSoup(res.content, 'lxml')
    authors = bsObj.find(attrs={"class": "auths"}).find_all('a')
    lst_authors = [author.get_text() for author in authors]
    if len(lst_authors) > 3:
        for i in range(3):
            result += lst_authors[i] + ', '
        result += 'et al '
    else:
        for idx, author in enumerate(lst_authors):
            if idx == len(lst_authors) - 1:
                result += author + " "
            else:
                result += author + ', '
    return result


def get_full_ref(author, title):
    result = author
    try:
        data_ref = get_data_ref(author + title)
    except:
        data_ref = get_data_ref(title)
    try:
        result += '(' + data_ref['year'] + '), "' + \
            title + '", *' + data_ref['journal'] + '*, '
    except:
        title = data_ref['title'].replace('--', '-')
        result += '(' + data_ref['year'] + '), "' + \
            title + '", *' + data_ref['journal'] + '*, '
    try:
        if data_ref['volume']:
            result += data_ref['volume']
            try:
                if data_ref['number']:
                    result += '(' + data_ref['number'] + ')'
            except:
                result += ''
            result += ', '
    except:
        result += ''
    pages = data_ref['pages']
    result += 'pp.' + pages.replace('--', '-') + '.'
    return result


order_and_title = get_order_and_title()
dict_ref = {}
for idx, order in enumerate(order_and_title):
    title = order_and_title.get(order)
    if title != '':
        try:
            authors = get_author_pm_by_title(title)
            dict_ref.update({(idx + 1): get_full_ref(authors, title)})
        except:
            if idx + 1 == 9:
                authors = get_author_pm_by_doi('10.1002/jcb.20532')
            elif idx + 1 == 16:
                authors = get_author_pm_by_doi('10.1517/13543784.16.5.659')
            elif idx + 1 == 18:
                authors = get_author_pm_by_doi('10.1016/j.bmcl.2006.09.002')
            elif idx + 1 == 26:
                authors = refactor_author(get_author(title))
            elif idx + 1 == 27:
                authors = get_author_pm_by_doi('10.1002/cmdc.200700314')
            elif idx + 1 == 12:
                authors = get_author_pm_by_doi('10.1038/sj.onc.1210610')
            if (authors):
                dict_ref.update({(idx + 1): get_full_ref(authors, title)})


lst_order_authors = [i for i in sorted(
    list(dict_ref.values()), cmp=collator.compare)]


for idx, ref in enumerate(lst_order_authors):
    for k, v in dict_ref.iteritems():
        if v == ref:
            print str(k) + ' -> ' + str(idx + 2) + '. ' + ref


for idx, ref in enumerate(lst_order_authors):
    for k, v in dict_ref.iteritems():
        if v == ref:
            print str(idx + 2) + '. ' + ref
