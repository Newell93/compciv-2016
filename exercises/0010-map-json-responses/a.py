import requests
import os
os.makedirs("tempdata/googlemaps", exist_ok = True)
os.makedirs("tempdata", exist_ok = True)
os.makedirs("tempdata/mapzen", exist_ok = True)
zipurl = 'http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json'
resp = requests.get(zipurl)
print(len(resp.text.splitlines()))
print(len(resp.text))
zname = os.path.join('tempdata', 'googlemaps', "stanford.json")
zfile = open(zname, 'wb')
zfile.write(resp.content)
zfile.close()
zipurl = 'http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json'
print(len("".splitlines()))
resp = requests.get(zipurl)
print(len(resp.text.splitlines()))
print(len(resp.text))
zname = os.path.join('tempdata', 'mapzen', "stanford.json")
zfile = open(zname, 'wb')
zfile.write(resp.content)
zfile.close()
