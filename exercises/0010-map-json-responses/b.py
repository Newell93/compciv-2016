import requests
import json
URL = 'http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json'
txt = requests.get(URL).text
mydict = json.loads(txt)
print(mydict['status'])