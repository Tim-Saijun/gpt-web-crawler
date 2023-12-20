import requests
url = "http://127.0.0.1:5000/craw_sigle_page"
paramt = {"url": "https://www.leadong.com/corporate-culture.html"}
r = requests.get(url, params=paramt)
print(r.text)