import requests
import os 
os.makedirs("tempdata", exist_ok = True)
os.makedirs("tempdata/ssa-babynames-nationwide-2014", exist_ok = True)
zipurl = 'http://stash.compciv.org/ssa_baby_names/ssa-babynames-nationwide-2014.txt'
resp = requests.get(zipurl)
mytext =(len(resp.text.splitlines()))
zname = os.path.join('tempdata', 'ssa-babynames-nationwide-2014', "babies")
zfile = open(zname, 'wb')
zfile.write(resp.content)
zfile.close()