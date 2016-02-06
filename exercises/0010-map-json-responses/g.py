import requests
import json
URL = 'http://www.compciv.org/files/datadumps/apis/mapzen/search-stanford.json'
txt = requests.get(URL).text
mydict = json.loads(txt)
thelabel = mydict["features"][0]["properties"]["label"]
theconfidence = mydict["features"][0]["properties"]["confidence"]
coord = mydict["features"][0]["geometry"]["coordinates"]
for c in coord:
	print(thelabel, ";",
	theconfidence, ";",
	coord)
thesecondlabel = mydict["features"][1]["properties"]["label"]
thesecondconfidence = mydict["features"][1]["properties"]["confidence"]
secondcoord = mydict["features"][1]["geometry"]["coordinates"]
for c in secondcoord:
	print(thesecondlabel, ";",
	thesecondconfidence, ";",
	secondcoord)
thethirdlabel = mydict["features"][2]["properties"]["label"]
thethirdconfidence = mydict["features"][2]["properties"]["confidence"]
thirdcoord = mydict["features"][2]["geometry"]["coordinates"]
for c in thirdcoord:
	print(thethirdlabel, ";",
	thethirdconfidence, ";",
	thirdcoord)
thefourthlabel = mydict["features"][3]["properties"]["label"]
thefourthconfidence = mydict["features"][3]["properties"]["confidence"]
fourthcoord = mydict["features"][3]["geometry"]["coordinates"]
for c in coord:
	print(thefourthlabel, ";",
	thefourthconfidence, ";",
	fourthcoord)
thefifthlabel = mydict["features"][4]["properties"]["label"]
thefifthconfidence = mydict["features"][4]["properties"]["confidence"]
fifthcoord = mydict["features"][4]["geometry"]["coordinates"]
for c in coord:
	print(thefifthlabel, ";",
	thefifthconfidence, ";",
	fifthcoord)
thesixthlabel = mydict["features"][5]["properties"]["label"]
thesixthconfidence = mydict["features"][5]["properties"]["confidence"]
sixthcoord = mydict["features"][5]["geometry"]["coordinates"]
for c in coord:
	print(thesixthlabel, ";",
	thesixthconfidence, ";",
	sixthcoord)
thesevlabel = mydict["features"][6]["properties"]["label"]
thesevconfidence = mydict["features"][6]["properties"]["confidence"]
sevcoord = mydict["features"][6]["geometry"]["coordinates"]
for c in coord:
	print(thesevlabel, ";",
	thesevconfidence, ";",
	sevcoord)
theeighlabel = mydict["features"][7]["properties"]["label"]
theeighconfidence = mydict["features"][7]["properties"]["confidence"]
eighcoord = mydict["features"][7]["geometry"]["coordinates"]
for c in coord:
	print(theeighlabel, ";",
	theeighconfidence, ";",
	eighcoord)
theninelabel = mydict["features"][8]["properties"]["label"]
thenineconfidence = mydict["features"][8]["properties"]["confidence"]
ninecoord = mydict["features"][8]["geometry"]["coordinates"]
for c in coord:
	print(theninelabel, ";",
	thenineconfidence, ";",
	ninecoord)
thetenlabel = mydict["features"][9]["properties"]["label"]
thetenconfidence = mydict["features"][9]["properties"]["confidence"]
tencoord = mydict["features"][9]["geometry"]["coordinates"]
for c in coord:
	print(thetenlabel, ";",
	thetenconfidence, ";",
	tencoord)