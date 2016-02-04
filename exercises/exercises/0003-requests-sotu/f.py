import requests
resp = requests.get("https://www.whitehouse.gov/the-press-office/remarks-president-barack-obama-address-joint-session-congress")
print (resp.url)
print(len(resp.text))
print(resp.text.upper().count('APPLAUSE'))
import requests
a = requests.get("https://www.whitehouse.gov/the-press-office/remarks-president-state-union-address")
print(a.url)
print(len(a.text))
print(a.text.upper().count('APPLAUSE'))
import requests
beat = requests.get("https://www.whitehouse.gov/the-press-office/2011/01/25/remarks-president-state-union-addressehouse.gov/the-press-office/2012/01/24/remarks-president-state-union-address")
print(beat.url)
print(len(beat.text))
print(beat.text.upper().count('APPLAUSE'))
import requests
c = requests.get("https://www.whitehouse.gov/the-press-office/2013/02/12/remarks-president-state-union-address")
print(c.url)
print(len(c.text))
print(c.text.upper().count('APPLAUSE'))
import requests
d = requests.get("https://www.whitehouse.gov/the-press-office/2014/01/28/president-barack-obamas-state-union-address")
print(d.url)
print(len(d.text))
print(d.text.upper().count('APPLAUSE'))
import requests
e = requests.get("https://www.whitehouse.gov/the-press-office/2015/01/20/remarks-president-state-union-address-january-20-2015")
print(e.url)
print(len(e.text))
print(e.text.upper().count('APPLAUSE'))
import requests
f = requests.get("https://www.whitehouse.gov/the-press-office/2016/01/12/remarks-president-barack-obama-%E2%80%93-prepared-delivery-state-union-address")
print(f.url)
print(len(f.text))
print(f.text.upper().count('APPLAUSE'))