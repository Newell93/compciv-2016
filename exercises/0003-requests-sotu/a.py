import requests
resp = requests.get("http://www.example.com")
print(requests.get("http://www.example.com"))
print(len(resp.text))
print(resp.url)