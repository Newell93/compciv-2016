import os
import requests
import shutil
os.makedirs("tempdata", exist_ok=True)
zipurl = 'http://stash.compciv.org/scrapespeare/matty.shakespeare.tar.gz'
resp = requests.get(zipurl)
zipdata = resp.content
zname = os.path.join("tempdata", "matty.shakespeare.tar.gz")
zfile = open(zname, "wb")
zfile.write(zipdata) 
zfile.close()
shutil.unpack_archive(zname, extract_dir='tempdata')
import os
fname = os.path.join("tempdata", "tragedies", "hamlet")
f = open(fname, 'r')
for x in range(25):
    print(f.readline().strip())
f.close()