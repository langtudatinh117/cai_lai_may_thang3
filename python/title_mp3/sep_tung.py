# coding=utf-8
from mutagen.mp3 import EasyMP3 as MP3

audio = MP3("noi_nay_co_anh.mp3")

print audio.pprint()

audio["title"] = u"世界"
audio.save()

print audio.pprint()