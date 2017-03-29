import urllib3
urllib3.disable_warnings()
http = urllib3.PoolManager()
r = http.request('GET', 'https://api.ipify.org/')
print (r.data)