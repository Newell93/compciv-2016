import os
import requests
import shutil
os.makedirs("tempdata", exist_ok=True)
zipurl = 'http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json'
resp = requests.get(zipurl)
zipdata = resp.content
zname = os.path.join("tempdata", "tempdata/googlemaps/stanford.json")
zfile = open(zname, "wb")
zfile.write(zipdata)
zfile.close()
shutil.unpack_archive(zname, extract_dir='tempdata')