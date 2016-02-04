import requests
import json
URL = 'http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json'
txt = requests.get(URL).text
mydict = json.loads(txt)
results = mydict["results"]
for r in results:
	geom = r['geometry']
	for g in geom:
		loc = r['location']
		for l in loc:
		print(l)
