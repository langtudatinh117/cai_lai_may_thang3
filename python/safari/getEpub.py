import accNoExp
import accSafariBook
import requests
import re
import urllib

# testfile = urllib.URLopener()
# testfile.retrieve("https://www.safaribooksonline.com/library/view/secrets-of-the/9781617292859/cover.jpg", "./img/cover.jpg")

def get_session():
    acc = accNoExp.get()
    s = accSafariBook.login(acc['username'], acc['password'])
    return s


def get_id_book(URL):
    for id_book in URL.split('/'):
        if re.match('^\d+$', id_book):
            return id_book

print accNoExp.get()
print get_id_book("https://www.safaribooksonline.com/api/v1/book/9781617292859/chapter/kindle_split_001.html")
