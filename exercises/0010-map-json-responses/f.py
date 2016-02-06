import requests
import json
URL = 'http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json'
txt = requests.get(URL).text
mydict = json.loads(txt)
thetype = mydict["type"]
thetext = mydict["geocoding"]["query"]["text"]
thesize = mydict["geocoding"]["query"]["size"]
theboundary = mydict["geocoding"]["query"]["boundary.country"]
print("type:", thetype, ",",
	"text:", thetext, ",",
	"size:", thesize, ",",
	"boundary.country:", theboundary)