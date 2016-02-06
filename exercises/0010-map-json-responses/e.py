import requests
import json
URL = 'http://www.compciv.org/files/datadumps/apis/googlemaps/geocode-stanford.json'
txt = requests.get(URL).text
mydict = json.loads(txt)
longitude = mydict["results"][0]["geometry"]["location"]["lng"]
latitude = mydict["results"][0]["geometry"]["location"]["lat"]
for x in mydict["results"]:
	print(longitude, ';',
	latitude, ';',
	x['formatted_address'])