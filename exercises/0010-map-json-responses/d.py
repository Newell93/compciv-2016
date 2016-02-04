import requests
import json
URL = 'http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json'
txt = requests.get(URL).text
mydict = json.loads(txt)
results = mydict["results"]
for r in results:
	components = r['address_components']
	for c in components:
		print(c['long_name'])